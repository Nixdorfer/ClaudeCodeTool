import json
import lancedb
import pyarrow as pa
from pathlib import Path

CHUNKS_SCHEMA = pa.schema([
    pa.field("id", pa.utf8()),
    pa.field("file_path", pa.utf8()),
    pa.field("start_line", pa.int32()),
    pa.field("end_line", pa.int32()),
    pa.field("content", pa.utf8()),
    pa.field("symbol_name", pa.utf8()),
    pa.field("symbol_type", pa.utf8()),
    pa.field("language", pa.utf8()),
    pa.field("signature", pa.utf8()),
    pa.field("context", pa.utf8()),
    pa.field("vector", pa.list_(pa.float32(), 768)),
])


class Store:
    def __init__(self, data_dir: Path):
        self._data_dir = data_dir
        self._data_dir.mkdir(parents=True, exist_ok=True)
        self._db = lancedb.connect(str(data_dir / "lancedb"))
        self._table = self.get_or_create_table()
        self._hashes_path = data_dir / "hashes.json"
        self._hashes: dict[str, str] = self._load_hashes()

    def get_or_create_table(self):
        if "chunks" in self._db.table_names():
            return self._db.open_table("chunks")
        return self._db.create_table("chunks", schema=CHUNKS_SCHEMA)

    def upsert_chunks(self, records: list[dict]):
        if not records:
            return
        ids = [r["id"] for r in records]
        id_list = ", ".join(f"'{i}'" for i in ids)
        try:
            self._table.delete(f"id IN ({id_list})")
        except Exception:
            pass
        self._table.add(records)

    def delete_by_file(self, file_path: str):
        self._table.delete(f"file_path = '{file_path}'")

    def search_vector(self, query_vec, top_k: int, file_pattern: str = "") -> list[dict]:
        q = self._table.search(query_vec).limit(top_k * 3)
        if file_pattern:
            q = q.where(f"file_path LIKE '%{file_pattern}%'")
        results = q.to_list()
        return results[:top_k]

    def get_all_contents(self, file_pattern: str = "") -> list[dict]:
        tbl = self._table.to_pandas()
        if file_pattern:
            tbl = tbl[tbl["file_path"].str.contains(file_pattern, na=False)]
        return tbl[["id", "content", "symbol_name", "file_path"]].to_dict("records")

    def find_symbol(self, name: str, sym_type: str = "") -> list[dict]:
        condition = f"symbol_name LIKE '%{name}%'"
        if sym_type:
            condition += f" AND symbol_type = '{sym_type}'"
        return self._table.search().where(condition).to_list()

    def get_file_symbols(self, file_path: str) -> list[dict]:
        results = self._table.search().where(f"file_path = '{file_path}'").to_list()
        return sorted(results, key=lambda r: r["start_line"])

    def get_stats(self) -> dict:
        df = self._table.to_pandas()
        total_files = df["file_path"].nunique() if len(df) else 0
        total_chunks = len(df)
        db_path = self._data_dir / "lancedb"
        db_size = sum(f.stat().st_size for f in db_path.rglob("*") if f.is_file()) if db_path.exists() else 0
        return {
            "total_files": total_files,
            "total_chunks": total_chunks,
            "db_size_mb": round(db_size / 1024 / 1024, 2),
        }

    def _load_hashes(self) -> dict[str, str]:
        if self._hashes_path.exists():
            return json.loads(self._hashes_path.read_text(encoding="utf-8"))
        return {}

    def file_needs_index(self, file_path: str, content_hash: str) -> bool:
        return self._hashes.get(file_path) != content_hash

    def mark_indexed(self, file_path: str, content_hash: str):
        self._hashes[file_path] = content_hash

    def save_hashes(self):
        self._hashes_path.write_text(json.dumps(self._hashes, ensure_ascii=False), encoding="utf-8")

    def get_indexed_files(self) -> set[str]:
        return set(self._hashes.keys())
