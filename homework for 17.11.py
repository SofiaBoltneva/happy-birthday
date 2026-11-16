
import requests
import os
#Этап 1 - Разведка
name = input("Введите имя: ")
user_id = int(input("Введите свой номер по журналу: "))
try:
    #Получаем предполагаемый возраст
    age_response = requests.get(
        "https://api.agify.io",
        params={"name": name},
        timeout=5)
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data["age"]
    #Получаем предполагаемый пол
    gender_response = requests.get(
        "https://api.genderize.io",
        params={"name": name},
        timeout=5)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    probability = gender_data["probability"]
    #Вычисляем вероятность женского пола
    if gender == "female":
        female_probability = probability * 100
    elif gender == "male":
        female_probability = (1 - probability) * 100
    else:
        female_probability = 0
    print("\nЭТАП 1")
    print(f"Цель: {name}")
    print(f"Вероятный возраст: {age}")
    print(f"Вероятность женского пола: {female_probability:.0f}%")

except requests.exceptions.RequestException as error:
    print("Ошибка при получении данных:", error)
    age = None
    gender = None
    female_probability = None

# Этап 2 - Маскировка
posts_count = 0
try:
    url = "https://jsonplaceholder.typicode.com/posts"
    #Заголовки запроса
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SecretAgentBot/1.0",
        "Accept-Language": "ru-RU,ru;q=0.9"}
    #Передаем номер пользователя через params
    response = requests.get(
        url,
        params={"userId": user_id},
        headers=headers,
        timeout=5)
    response.raise_for_status()
    posts = response.json()
    posts_count = len(posts)
    print("\nЭТАП 2")
    print("Количество постов:", posts_count)
    if posts:
        print("Заголовок первого поста:", posts[0]["title"])
    else:
        print("Посты не найдены")
except requests.exceptions.RequestException as error:
    print("Ошибка при получении постов:", error)

#Этап 3 - Передача данных
report = {
    "name": name,
    "age": age,
    "gender": gender,
    "posts_count": posts_count}
try:
    response = requests.post(
        "https://httpbin.org/post",
        json=report,
        timeout=5)
    response.raise_for_status()
    result = response.json()
    print("\nЭТАП 3")
    print("Данные успешно отправлены!")
    print("Полученный JSON:", result["json"])
except requests.exceptions.RequestException as error:
    print("Ошибка при отправке отчета:", error)

#Этап 4 - Загрузка улик
try:
    response = requests.get(
        "https://picsum.photos/400/300",
        stream=True,
        timeout=10)
    response.raise_for_status()
    #Сохраняем изображение частями
    with open("evidence.jpg", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    size = os.path.getsize("evidence.jpg")
    print("\nЭТАП 4")
    print("Изображение сохранено: evidence.jpg")
    print("Размер файла:", size, "байт")
except requests.exceptions.RequestException as error:
    print("Ошибка при скачивании изображения:", error)

#Этап 5 - Обработка сбоев
print("\nЭТАП 5")
try:
    #Cоздаем ошибку 404
    response = requests.get(
        "https://httpbin.org/status/404",
        timeout=3)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Ошибка: время ожидания ответа истекло!")
except requests.exceptions.HTTPError:
    print("Ошибка: сервер вернул HTTP-ошибку (404)!")
except requests.exceptions.RequestException as error:
    print("Ошибка соединения:", error)
try:
    #Сервер отвечает через 6 секунд, а мы ждем только 3
    response = requests.get(
        "https://httpbin.org/delay/6",
        timeout=3)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Ошибка: сервер не ответил за 3 секунды!")
except requests.exceptions.HTTPError:
    print("Ошибка HTTP!")
except requests.exceptions.RequestException as error:
    print("Ошибка соединения:", error)
print("\nРабота программы завершена!")
