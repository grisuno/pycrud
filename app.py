import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import csv
import os
import datetime

# Función para obtener una conexión a la base de datos
def get_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

# Función para obtener todos los registros de la tabla
def get_records(table_name):
    conn = get_connection(f"{table_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    conn.close()
    return rows

# Función para obtener un registro por ID
def get_record_by_id(table_name, id):
    conn = get_connection(f"{table_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name} WHERE id=?", (id,))
    row = c.fetchone()
    conn.close()
    return row

# Función para insertar un nuevo registro
def insert_record(table_name, data):
    conn = get_connection(f"{table_name}.db")
    c = conn.cursor()
    # Obtener la fecha de creación y modificación actual
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Insertar el nuevo registro con la fecha de creación y modificación actual
    c.execute(f"INSERT INTO {table_name} VALUES (NULL, {', '.join(['?' for i in range(len(data)+2)])})", data + [now, now])
    conn.commit()
    conn.close()

# Función para actualizar un registro existente
def update_record(table_name, id, data):
    conn = get_connection(f"{table_name}.db")
    c = conn.cursor()
    # Obtener la fecha de modificación actual
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Actualizar el registro con la fecha de modificación actual
    c.execute(f"UPDATE {table_name} SET {', '.join([f'{col}=?' for col in data.keys()])}, modificacion=? WHERE id=?", tuple(data.values()) + (now, id))
    conn.commit()
    conn.close()

# Función para eliminar un registro por ID
def delete_record(table_name, id):
    conn = get_connection(f"{table_name}.db")
    c = conn.cursor()
    c.execute(f"DELETE FROM {table_name} WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Función para crear la tabla en la base de datos
def create_table(csv_file):
    # Abrir el archivo CSV
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # Obtener los nombres de las columnas
        columns = next(reader)
        # Agregar la columna de ID, creacion y modificacion
        columns.insert(0, 'id')
        columns.append('creacion')
        columns.append('modificacion')

        # Crear la base de datos con el nombre del archivo
        db_name = os.path.splitext(csv_file)[0] + '.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Crear la tabla con los nombres de las columnas
        c.execute(f"CREATE TABLE {os.path.splitext(csv_file)[0]} ({', '.join(columns)})")

        # Insertar los datos del archivo CSV en la tabla
        for row in reader:
            # Obtener los valores del registro
            values = row
            # Agregar el ID del registro como NULL
            values.insert(0, 'NULL')
            # Agregar la fecha de creación y modificación del registro como la fecha actual
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            values.append(now)
            values.append(now)
            # Insertar el registro en la tabla
            c.execute(f"INSERT INTO {os.path.splitext(csv_file)[0]} VALUES ({', '.join(['?' for i in range(len(values))])})", values)

        # Cerrar la conexión a la base de datos
        conn.commit()
        conn.close()
def generate_crud():
    # Obtener el archivo CSV seleccionado
    csv_file = csv_file_entry.get()
    if not csv_file:
        messagebox.showerror("Error", "Debe seleccionar un archivo CSV")
        return
    # Crear la tabla en la base de datos
    create_table(csv_file)
    # Crear el archivo CRUD
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
    
    print(f"El archivo CRUD {os.path.splitext(csv_file)[0]}.js ha sido creado exitosamente.")
    print(f"Para iniciar el servidor, ejecuta 'node {os.path.splitext(csv_file)[0]}.js'")

# Función para crear la interfaz gráfica
def create_gui():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Mi aplicación")
    root.geometry("500x500")

    # Agregar etiqueta
    label = tk.Label(root, text="Bienvenido a mi aplicación!")
    label.pack()

    # Agregar botón para seleccionar archivo CSV
    def browse_csv_file():
        global csv_file_path, csv_file_entry
        csv_file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        csv_file_entry.delete(0, tk.END)
        csv_file_entry.insert(0, csv_file_path)
        generate_crud()  # Actualizar la tabla con los datos del archivo CSV seleccionado



    browse_button = tk.Button(root, text="Seleccionar archivo CSV", command=browse_csv_file)
    browse_button.pack()

    # Agregar campo de entrada de texto para mostrar la ruta del archivo CSV seleccionado
    csv_file_entry = tk.Entry(root, width=50)
    #csv_file_entry.grid(row=1, column=1, padx=10, pady=10)
    csv_file_entry.pack()

    # Agregar botón para generar CRUD
    
    generate_button = tk.Button(root, text="Generar CRUD", command=generate_crud)
    generate_button.pack()

    root.mainloop()



def create_label(root, text):
    label = tk.Label(root, text=text)
    label.pack()

def create_button(root, text, command):
    button = tk.Button(root, text=text, command=command)
    button.pack()

def button_click():
    print("Button clicked!")

def main():
    create_gui()

if __name__ == "__main__":
    main()
