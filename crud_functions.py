import sqlite3

connection = sqlite3.connect("module 14/initiate.db")
curs = connection.cursor()

curs.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
)
''')

for i in range(1, 5):
    curs.execute("INSERT INTO Users (id, title, description, price ) VALUES (?, ?, ?, ?)", (f"{i}", f"Продукт{i}", f"Описание{i}", f"{i * 100}"))

def get_all_products(id, title, description, price):
    full = [id, title, description, price]
    return full

connection.commit()
connection.close()