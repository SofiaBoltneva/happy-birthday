import requests
#Словарь с описанием погодных условий
WEATHER_CODES = {
    0: "☀️ Ясно",
    1: "🌤️ Преимущественно ясно",
    2: "⛅ Переменная облачность",
    3: "☁️ Пасмурно",
    45: "🌫️ Туман",
    48: "🌫️ Иней",
    51: "🌦️ Легкая морось",
    53: "🌦️ Морось",
    55: "🌧️ Сильная морось",
    61: "🌧️ Небольшой дождь",
    63: "🌧️ Дождь",
    65: "🌧️ Сильный дождь",
    71: "🌨️ Небольшой снег",
    73: "🌨️ Снег",
    75: "🌨️ Сильный снег",
    80: "🌦️ Ливень",
    95: "⛈️ Гроза",
    96: "⛈️ Гроза с градом"}
#Получение координат города
def get_city_coordinates(city_name):
    try:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        response = requests.get(url,
            params={
                "name": city_name,
                "count": 1,
                "language": "ru"},
            timeout=5)
        response.raise_for_status()
        data = response.json()
        if not data.get("results"):
            print(f"Город '{city_name}' не найден. Проверьте название.")
            return None
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
        return lat, lon
    except requests.exceptions.Timeout:
        print("Ошибка: время ожидания ответа истекло.")
    except requests.exceptions.HTTPError:
        print("Ошибка HTTP при поиске города.")
    except requests.exceptions.ConnectionError:
        print("Ошибка сети. Проверьте подключение к интернету.")
    except ValueError:
        print("Ошибка: сервер вернул некорректный JSON.")
    return None
#Получение погоды
def get_weather(lat, lon):
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        response = requests.get(url,
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
                "timezone": "auto" },
            timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["current"]
    except requests.exceptions.Timeout:
        print("Ошибка: время ожидания ответа истекло.")
    except requests.exceptions.HTTPError:
        print("Ошибка HTTP при получении погоды.")
    except requests.exceptions.ConnectionError:
        print("Ошибка сети. Проверьте подключение к интернету.")
    except (ValueError, KeyError):
        print("Ошибка: некорректный ответ сервера.")
    return None
#Перевод погодного кода в текст
def decode_weather_code(code):
    return WEATHER_CODES.get(
        code,
        f"Неизвестные условия (код: {code})")
def format_weather_output(city, weather_data):
    temperature = weather_data["temperature_2m"]
    humidity = weather_data["relative_humidity_2m"]
    wind = weather_data["wind_speed_10m"]
    code = weather_data["weather_code"]
    weather_description = decode_weather_code(code)
    result = (
        f"\nПогода в городе: {city}\n"
        f"Температура: {temperature:+.0f}°C\n"
        f"Влажность: {humidity}%\n"
        f"Ветер: {wind} км/ч\n"
        f"Состояние: {weather_description}")
    return result
city = input("Введите название города на английском: ").strip()
if not city:
    print("Ошибка: название города не может быть пустым.")
else:
    coordinates = get_city_coordinates(city)
    if coordinates is not None:
        lat, lon = coordinates
        weather_data = get_weather(lat, lon)
        if weather_data is not None:
            print(format_weather_output(city, weather_data))
