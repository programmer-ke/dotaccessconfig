## MVP spec

| Topic | Decision |
|-------|----------|
| **Mutability** | Immutable after construction. |
| **Value types** | Preserved (int, float, bool, list, None, etc.). |
| **Constructor** | `Config(dict)` – default. |
| **Alternate constructors** | `Config.from_json(path_or_file)` and `Config.from_yaml(path_or_file)`. |
| **Nested dicts** | Automatically converted to recursive `Config` objects (dot‑accessible). |
| **Lists of dicts** | Dicts inside lists also become `Config` objects. |
| **Invalid identifiers** | Accessible only via `config['key']`. Dot‑notation skipped. |
| **`__repr__`/`__str__`** | Flat representation. |
| **Iteration / `len`** | Out of scope for MVP. |
