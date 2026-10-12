import json
with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)
cities = {} #пустой словарь для хранения пользователей
for user in users: #перебираем каждого пользователя из списка
    city = user["address"]["city"]
    name = user["name"]
    if city not in cities: #проверяем, есть ли этот город
        cities[city] = []
    cities[city].append(name)
with open("cities.json", "w", encoding="utf-8") as file: #файл для записи результата
    json.dump(cities, file, ensure_ascii=False, indent=4)
print("Результат сохранён в cities.json")
