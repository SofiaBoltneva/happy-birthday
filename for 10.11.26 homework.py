import json
from sqlalchemy import *
from sqlalchemy import *
from sqlalchemy import *
#Загружаем данные из JSON
with open("catalog.json", "r", encoding="utf-8") as file:
    catalog = json.load(file)
engine = create_engine("sqlite:///shop.db")
metadata = MetaData()
#Создаем таблицу категорий
categories = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("description", String))
#Создаем таблицу товаров
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_name", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id")))
metadata.create_all(engine)
#Собираем категории и товары
category_data = {}
product_data = []
for item in catalog:
    category = item["category"]
    name = category["name"]
    category_data[name] = category["description"]
    product_data.append({
        "product_name": item["product_name"],
        "price": item["price"],
        "category_name": name})
#Добавляем данные в базу
with engine.begin() as connection:
    #Очищаем старые данные
    connection.execute(products.delete())
    connection.execute(categories.delete())
    #Добавляем категории
    for name, description in category_data.items():
        connection.execute(
            insert(categories).values(
                name=name,
                description=description))
    #Получаем ID категорий
    result = connection.execute(
        select(categories.c.id, categories.c.name))
    category_ids = {}
    for row in result:
        category_ids[row.name] = row.id
    #Добавляем товары
    for item in product_data:
        connection.execute(insert(products).values(
                product_name=item["product_name"],
                price=item["price"],
                category_id=category_ids[item["category_name"]]))
    #Считаем количество категорий и товаров
    categories_count = connection.execute(
        select(func.count()).select_from(categories)).scalar()
    products_count = connection.execute(
        select(func.count()).select_from(products)).scalar()
    print("Количество категорий:", categories_count)
    print("Количество товаров:", products_count)
    #Выводим товары вместе с категориями
    result = connection.execute(
        select(
            products.c.product_name,
            products.c.price,
            categories.c.name).select_from(products.join(categories)))
    print("\nСписок товаров:")
    for row in result:
        print(
            f"Товар: {row.product_name}, "
            f"Цена: {row.price}, "
            f"Категория: {row.name}")
print("\nРабота программы завершена!")