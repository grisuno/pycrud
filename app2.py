import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import csv
import os
import datetime

# Punto 1: Dividir en funciones más pequeñas
def get_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def get_records(table_name):
    conn = get_connection(f"{table_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    conn.close()
    return rows

def create_table(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        columns = next(reader)
        columns.insert(0, 'id')
        columns.append('creacion')
        columns.append('modificacion')

        db_name = os.path.splitext(csv_file)[0] + '.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute(f"CREATE TABLE {os.path.splitext(csv_file)[0]} ({', '.join(columns)})")

        for row in reader:
            values = row
            values.insert(0, 'NULL')
            values.append(get_current_datetime())
            values.append(get_current_datetime())
            c.execute(f"INSERT INTO {os.path.splitext(csv_file)[0]} VALUES ({', '.join(['?' for i in range(len(values))])})", values)

        conn.commit()
        conn.close()

def generate_crud(csv_data):
    try:
        csv_file = csv_data.csv_file
        create_table(csv_file)
        with open(f"{os.path.splitext(csv_file)[0]}.js", 'w') as file:
            file.write(f"// CRUD para la tabla {os.path.splitext(csv_file)[0]}\n")
            file.write(f"const express = require('express');\n")
            file.write(f"const app = express();\n")
            file.write(f"const bodyParser = require('body-parser');\n")
            file.write(f"const sqlite3 = require('sqlite3').verbose();\n")
            file.write(f"const db = new sqlite3.Database('{os.path.splitext(csv_file)[0]}.db');\n")
            file.write(f"app.use(bodyParser.urlencoded({{ extended: true }}));\n\n")
            file.write(f"// Obtener todos los registros\n")
            file.write(f"app.get('/', (req, res) => {{\n")
            file.write(f"    db.all(`SELECT * FROM {os.path.splitext(csv_file)[0]}`, (err, rows) => {{\n")
            file.write(f"        if (err) {{\n")
            file.write(f"            console.error(err.message);\n")
            file.write(f"            res.status(500).send('Error del servidor');\n")
            file.write(f"        }} else {{\n")
            file.write(f"            res.json(rows);\n")
            file.write(f"        }}\n")
            file.write(f"    }});\n")
            file.write(f"}});\n\n")
            file.write(f"// Obtener un registro por ID\n")
            file.write(f"app.get('/:id', (req, res) => {{\n")
            file.write(f"    db.get(`SELECT * FROM {os.path.splitext(csv_file)[0]} WHERE id=?`, [req.params.id], (err, row) => {{\n")
            file.write(f"        if (err) {{\n")
            file.write(f"            console.error(err.message);\n")
            file.write(f"            res.status(500).send('Error del servidor');\n")
            file.write(f"        }} else if (!row) {{\n")
            file.write(f"            res.status(404).send('Registro no encontrado');\n")
            file.write(f"        }} else {{\n")
            file.write(f"            res.json(row);\n")
            file.write(f"        }}\n")
            file.write(f"    }});\n")
            file.write(f"}});\n\n")
            file.write(f"// Agregar un nuevo registro\n")
            file.write(f"app.post('/', (req, res) => {{\n")
            file.write(f"    const values = Object.values(req.body);\n")
            file.write(f"    db.run(`INSERT INTO {os.path.splitext(csv_file)[0]} VALUES (${', '.join(['?' for i in range(len(values) + 2)])})`, [...values, null, new Date()], (err) => {{\n")
            file.write(f"        if (err) {{\n")
            file.write(f"            console.error(err.message);\n")
            file.write(f"            res.status(500).send('Error del servidor');\n")
            file.write(f"        }} else {{\n")
            file.write(f"            res.send('Registro agregado correctamente');\n")
            file.write(f"        }}\n\n")
            file.write(f"    }});\n")
            file.write(f"}});\n\n")
            file.write(f"// Actualizar un registro existente\n")
            file.write(f"app.put('/:id', (req, res) => {{\n")
            file.write(f"    const values = Object.values(req.body);\n")
            file.write(f"    db.run(`UPDATE {os.path.splitext(csv_file)[0]} SET {', '.join([f'{col}=?' for col in headers[1:]])}, modificacion=? WHERE id=?`, [...values, new Date(), req.params.id], (err) => {{\n")
            file.write(f"        if (err) {{\n")
            file.write(f"            console.error(err.message);\n")
            file.write(f"            res.status(500).send('Error del servidor');\n")
            file.write(f"        }} else if (this.changes === 0) {{\n")
            file.write(f"            res.status(404).send('Registro no encontrado');\n")
            file.write(f"        }} else {{\n")
            file.write(f"            res.send('Registro actualizado correctamente');\n")
            file.write(f"        }}\n")
            file.write(f"    }});\n")
            file.write(f"}});\n\n")
            file.write(f"// Eliminar un registro existente\n")
            file.write(f"app.delete('/:id', (req, res) => {{\n")
            file.write(f"    db.run(`DELETE FROM {os.path.splitext(csv_file)[0]} WHERE id=?`, [req.params.id], (err) => {{\n")
            file.write(f"        if (err) {{\n")
            file.write(f"            console.error(err.message);\n")
            file.write(f"            res.status(500).send('Error del servidor');\n")
            file.write(f"        }} else if (this.changes === 0) {{\n")
            file.write(f"            res.status(404).send('Registro no encontrado');\n")
            file.write(f"        }} else {{\n")
            file.write(f"            res.send('Registro eliminado correctamente');\n")
            file.write(f"        }}\n")
            file.write(f"    }});\n")
            file.write(f"}});\n\n")
            file.write(f"app.listen(3000, () => console.log(`Servidor iniciado en el puerto 3000`));\n")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Punto 4: Usar una clase o estructura de datos
class CSVData:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.csv_data = None

    def load_csv_data(self):
        with open(self.csv_file, 'r') as file:
            self.csv_data = list(csv.reader(file))

# Punto 6: Usar convenciones de estilo de código
def get_current_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def create_gui():
    root = tk.Tk()
    root.title("Mi aplicación")
    root.geometry("500x500")

    label = tk.Label(root, text="Bienvenido a mi aplicación!")
    label.pack()

    def browse_csv_file():
        global csv_file_path, csv_file_entry
        csv_file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        csv_file_entry.delete(0, tk.END)
        csv_file_entry.insert(0, csv_file_path)
        csv_data = CSVData(csv_file_path)
        generate_crud(csv_data)

    browse_button = tk.Button(root, text="Seleccionar archivo CSV", command=browse_csv_file)
    browse_button.pack()

    csv_file_entry = tk.Entry(root, width=50)
    csv_file_entry.pack()

    generate_button = tk.Button(root, text="Generar CRUD", command=lambda: generate_crud(csv_data))
    generate_button.pack()

    root.mainloop()

def main():
    create_gui()

if __name__ == "__main__":
    main()
