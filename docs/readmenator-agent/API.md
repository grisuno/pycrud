# API

## app.py
- `get_connection` (function) `app.py:9` `def get_connection(db_file)`
- `get_records` (function) `app.py:15` `def get_records(table_name)`
- `get_record_by_id` (function) `app.py:24` `def get_record_by_id(table_name, id)`
- `insert_record` (function) `app.py:33` `def insert_record(table_name, data)`
- `update_record` (function) `app.py:44` `def update_record(table_name, id, data)`
- `delete_record` (function) `app.py:55` `def delete_record(table_name, id)`
- `create_table` (function) `app.py:63` `def create_table(csv_file)`
- `generate_crud` (function) `app.py:98` `def generate_crud()`
- `create_gui` (function) `app.py:184` `def create_gui()`
- `browse_csv_file` (function) `app.py:195` `def browse_csv_file()`
- `create_label` (function) `app.py:221` `def create_label(root, text)`
- `create_button` (function) `app.py:225` `def create_button(root, text, command)`
- `button_click` (function) `app.py:229` `def button_click()`
- `main` (function) `app.py:232` `def main()`

## app2.py
- `get_connection` (function) `app2.py:9` `def get_connection(db_file)`
- `get_records` (function) `app2.py:14` `def get_records(table_name)`
- `create_table` (function) `app2.py:22` `def create_table(csv_file)`
- `generate_crud` (function) `app2.py:46` `def generate_crud(csv_data)`
- `CSVData.__init__` (method) `app2.py:128` `def __init__(self, csv_file)`
- `CSVData.load_csv_data` (method) `app2.py:132` `def load_csv_data(self)`
- `CSVData.get_current_datetime` (method) `app2.py:137` `def get_current_datetime()`
- `CSVData.create_gui` (method) `app2.py:140` `def create_gui()`
- `CSVData.browse_csv_file` (method) `app2.py:148` `def browse_csv_file()`
- `CSVData.main` (method) `app2.py:167` `def main()`
