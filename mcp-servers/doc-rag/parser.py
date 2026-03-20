import os
import re
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum


class ElementType(Enum):
    TITLE = "title"
    TEXT = "text"
    TABLE = "table"
    IMAGE = "image"
    LIST = "list"
    CODE = "code"


@dataclass
class DocElement:
    type: ElementType
    text: str
    page: int | None = None
    metadata: dict = field(default_factory=dict)


class DocumentParser:
    def __init__(self, config: dict, device: str):
        self.config = config
        self.device = device
        parser_cfg = config.get("parser", {})
        self.mineru_enabled: bool = parser_cfg.get("mineru_enabled", False)
        self.fallback_to_docling: bool = parser_cfg.get("fallback_to_docling", True)
        ocr_cfg = parser_cfg.get("ocr", {})
        self.paddleocr_enabled: bool = ocr_cfg.get("paddleocr_enabled", False)
        self.paddleocr_use_onnx: bool = ocr_cfg.get("paddleocr_use_onnx", True)
        self.tesseract_lang: str = ocr_cfg.get("tesseract_lang", "deu+eng")

    async def parse(self, file_path: str) -> list[DocElement]:
        ext = Path(file_path).suffix.lower()
        if ext in (".md", ".txt"):
            return self._parse_text(file_path)
        if ext == ".pdf":
            return await self._parse_pdf(file_path)
        return self._parse_with_docling(file_path)

    def _parse_text(self, file_path: str) -> list[DocElement]:
        ext = Path(file_path).suffix.lower()
        text = Path(file_path).read_text(encoding="utf-8", errors="replace")
        if ext == ".md":
            return self._split_markdown(text)
        return self._split_plaintext(text)

    def _split_markdown(self, text: str) -> list[DocElement]:
        elements = []
        for line in text.splitlines():
            m = re.match(r"^(#{1,6})\s+(.+)", line)
            if m:
                elements.append(DocElement(type=ElementType.TITLE, text=m.group(2)))
            elif line.strip():
                elements.append(DocElement(type=ElementType.TEXT, text=line.strip()))
        return elements

    def _split_plaintext(self, text: str) -> list[DocElement]:
        blocks = re.split(r"\n{2,}", text)
        return [DocElement(type=ElementType.TEXT, text=b.strip()) for b in blocks if b.strip()]

    def _parse_with_docling(self, file_path: str) -> list[DocElement]:
        from docling.document_converter import DocumentConverter
        converter = DocumentConverter()
        result = converter.convert(file_path)
        elements = []
        for item in result.document.texts:
            label = getattr(item, "label", "text")
            etype = ElementType.TITLE if "title" in str(label).lower() or "heading" in str(label).lower() else ElementType.TEXT
            elements.append(DocElement(type=etype, text=item.text))
        for item in result.document.tables:
            md = item.export_to_markdown()
            elements.append(DocElement(type=ElementType.TABLE, text=md))
        return elements

    async def _parse_pdf(self, file_path: str) -> list[DocElement]:
        lang = self._detect_pdf_language(file_path)
        if lang == "ch" and self.mineru_enabled:
            try:
                return self._parse_with_mineru(file_path)
            except Exception:
                if self.fallback_to_docling:
                    return self._parse_with_docling(file_path)
                raise
        return self._parse_with_docling(file_path)

    def _parse_with_mineru(self, file_path: str) -> list[DocElement]:
        from magic_pdf.data.data_reader_writer import FileBasedDataWriter
        from magic_pdf.data.dataset import PymuDocDataset
        from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze
        from magic_pdf.config.enums import SupportedPdfParseMethod

        ds = PymuDocDataset(open(file_path, "rb").read())
        method = SupportedPdfParseMethod.AUTO
        infer_result = doc_analyze(ds, ocr=True)
        pipe = infer_result.get_infer_res()
        elements = []
        for block in pipe:
            text = block.get("text", "").strip()
            if not text:
                continue
            btype = block.get("type", "text")
            etype = ElementType.TABLE if btype == "table" else ElementType.TITLE if btype in ("title", "heading") else ElementType.TEXT
            elements.append(DocElement(type=etype, text=text, page=block.get("page")))
        return elements

    def _detect_pdf_language(self, file_path: str) -> str:
        from pdfminer.high_level import extract_text
        try:
            text = extract_text(file_path, maxpages=2)
        except Exception:
            return "en"
        if not text:
            return "en"
        chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
        ratio = chinese_chars / max(len(text), 1)
        if ratio > 0.2:
            return "ch"
        german_chars = len(re.findall(r"[äöüÄÖÜß]", text))
        if german_chars > 5:
            return "de"
        return "en"

    def _ocr_image(self, image_path: str, lang: str) -> str:
        if lang == "ch" and self.paddleocr_enabled:
            from paddleocr import PaddleOCR
            ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_onnx=self.paddleocr_use_onnx, show_log=False)
            result = ocr.ocr(image_path, cls=True)
            lines = []
            for block in (result or []):
                for item in (block or []):
                    if item and len(item) > 1:
                        lines.append(item[1][0])
            return "\n".join(lines)
        import pytesseract
        from PIL import Image
        return pytesseract.image_to_string(Image.open(image_path), lang=self.tesseract_lang)
