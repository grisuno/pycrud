# Subsystem: root

## app.py
- Layer: utility
- Language: py
- Symbols:
  - `get_connection` (function, line 9) `def get_connection(db_file)`
  - `get_records` (function, line 15) `def get_records(table_name)`
  - `get_record_by_id` (function, line 24) `def get_record_by_id(table_name, id)`
  - `insert_record` (function, line 33) `def insert_record(table_name, data)`
  - `update_record` (function, line 44) `def update_record(table_name, id, data)`
  - `delete_record` (function, line 55) `def delete_record(table_name, id)`
  - `create_table` (function, line 63) `def create_table(csv_file)`
  - `generate_crud` (function, line 98) `def generate_crud()`
  - `create_gui` (function, line 184) `def create_gui()`
  - `create_label` (function, line 221) `def create_label(root, text)`
  - `create_button` (function, line 225) `def create_button(root, text, command)`
  - `button_click` (function, line 229) `def button_click()`
  - `main` (function, line 232) `def main()`
  - `browse_csv_file` (function, line 195) `def browse_csv_file()`

## app2.py
- Layer: utility
- Language: py
- Symbols:
  - `get_connection` (function, line 9) `def get_connection(db_file)`
  - `get_records` (function, line 14) `def get_records(table_name)`
  - `create_table` (function, line 22) `def create_table(csv_file)`
  - `generate_crud` (function, line 46) `def generate_crud(csv_data)`
  - `CSVData` (class, line 127) `class CSVData`
  - `get_current_datetime` (method, line 137) `def get_current_datetime()`
  - `create_gui` (method, line 140) `def create_gui()`
  - `main` (method, line 167) `def main()`
  - `__init__` (method, line 128) `def __init__(self, csv_file)`
  - `load_csv_data` (method, line 132) `def load_csv_data(self)`
  - `browse_csv_file` (method, line 148) `def browse_csv_file()`
