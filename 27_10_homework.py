import json
import sqlite3
#Читаем данные из JSON-файла
with open("catalog.json", "r", encoding="utf-8") as file:
    catalog = json.load(file)
#Создаем подключение к базе данных SQLite
connection = sqlite3.connect("shop.db")
cursor = connection.cursor()
#Включаем проверку внешних ключей
cursor.execute("PRAGMA foreign_keys = ON")
#Создаем таблицу категорий
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT)""")
#Создаем таблицу товаров
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id))""")
#Перебираем товары из JSON-файла
for item in catalog:
    #Получаем данные категории
    category_name = item["category"]["name"]
    category_description = item["category"]["description"]
    #Добавляем категорию, если ее еще нет
    cursor.execute("""
    INSERT OR IGNORE INTO categories (name, description)
    VALUES (?, ?)""", (category_name, category_description))
    #Получаем ID категории
    cursor.execute("""
    SELECT id FROM categories
    WHERE name = ?
    """, (category_name,))
    category_id = cursor.fetchone()[0]
    #Добавляем товар в таблицу products
    cursor.execute("""
    INSERT INTO products (product_name, price, category_id)
    VALUES (?, ?, ?) """, (
        item["product_name"],
        item["price"],
        category_id
    ))
#Сохраняем изменения в базе данных
connection.commit()
#Выводим количество категорий
cursor.execute("SELECT COUNT(*) FROM categories")
print("Количество категорий:", cursor.fetchone()[0])
#Выводим количество товаров
cursor.execute("SELECT COUNT(*) FROM products")
print("Количество товаров:", cursor.fetchone()[0])
#Выводим товары вместе с категориями
cursor.execute("""
SELECT
    products.product_name,
    products.price,
    categories.name
FROM products
JOIN categories
ON products.category_id = categories.id""")
print("\nСписок товаров:")
for product in cursor.fetchall():
    print(
        f"Товар: {product[0]}, "
        f"Цена: {product[1]}, "
        f"Категория: {product[2]}"
    )
#Закрываем соединение с базой данных
connection.close()
print("\nРабота программы завершена!")
