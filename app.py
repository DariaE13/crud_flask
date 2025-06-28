import sqlite3
from flask import Flask, render_template, request, redirect, url_for


# Создание БД users
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NUL,
        last_name TEXT NOT NUL,
        gender TEXT NOT NUL,
        age INTEGER NOT NUL,
        phone TEXT NOT NUL,
        email TEXT NOT NUL,
        address TEXT NOT NULL,
        salary REAL NOT NULL
        
    )
               
""")

conn.commit()
conn.close()