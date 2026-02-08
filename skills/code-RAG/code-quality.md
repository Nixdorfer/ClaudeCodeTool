# Code Quality

### find_dead_code(language="")
Find defined but never-called functions. Skips main/new/Drop/trait methods/wasm_bindgen/tests.

### complexity_hotspots(directory="", top_n=30)
Top functions by cyclomatic complexity. Reports score, nesting depth, line count.

### detect_antipatterns(checks="", directory="")
Checks (comma-separated, ""=all): unbounded_collection, unsafe_block, todo_density, missing_dispose, large_function, deep_nesting, magic_numbers, error_swallow.

### find_orphans()
Find source files not imported by any other file.

### scan_annotations(annotation_type="")
Scan TODO/FIXME/HACK/XXX/BUG/NOTE/PERF/SAFETY markers. Filter by type.
