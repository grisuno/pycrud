# root

*Community 0 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `CSVData`, `__init__`, `browse_csv_file`, `button_click`, `create_button`, `create_gui`, `create_label`, `create_table`. Core file: `app.py` (14 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 14 | no |
| `app2.py` | py | utility | 11 | no |

## Key Symbols

- `get_connection` (function, `app.py:9`) `def get_connection(db_file)`
- `get_records` (function, `app.py:15`) `def get_records(table_name)`
- `get_record_by_id` (function, `app.py:24`) `def get_record_by_id(table_name, id)`
- `insert_record` (function, `app.py:33`) `def insert_record(table_name, data)`
- `update_record` (function, `app.py:44`) `def update_record(table_name, id, data)`
- `delete_record` (function, `app.py:55`) `def delete_record(table_name, id)`
- `create_table` (function, `app.py:63`) `def create_table(csv_file)`
- `generate_crud` (function, `app.py:98`) `def generate_crud()`
- `create_gui` (function, `app.py:184`) `def create_gui()`
- `browse_csv_file` (function, `app.py:195`) `def browse_csv_file()`
- `create_label` (function, `app.py:221`) `def create_label(root, text)`
- `create_button` (function, `app.py:225`) `def create_button(root, text, command)`
- `button_click` (function, `app.py:229`) `def button_click()`
- `main` (function, `app.py:232`) `def main()`
- `get_connection` (function, `app2.py:9`) `def get_connection(db_file)`
- `get_records` (function, `app2.py:14`) `def get_records(table_name)`
- `create_table` (function, `app2.py:22`) `def create_table(csv_file)`
- `generate_crud` (function, `app2.py:46`) `def generate_crud(csv_data)`
- `CSVData` (class, `app2.py:127`) `class CSVData`
- `__init__` (method, `app2.py:128`) `def __init__(self, csv_file)`
- `load_csv_data` (method, `app2.py:132`) `def load_csv_data(self)`
- `get_current_datetime` (method, `app2.py:137`) `def get_current_datetime()`
- `create_gui` (method, `app2.py:140`) `def create_gui()`
- `browse_csv_file` (method, `app2.py:148`) `def browse_csv_file()`
- `main` (method, `app2.py:167`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `app.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `app2.py`
