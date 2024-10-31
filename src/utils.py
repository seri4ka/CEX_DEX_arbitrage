import csv
import os
from datetime import datetime

# Путь к CSV файлу для хранения данных о ценах
file_path = "data/price_data.csv"

# Проверяем наличие файла; если его нет, создаем и добавляем заголовки
if not os.path.exists(file_path):
    os.makedirs("data", exist_ok=True)  # Создаем папку data, если её нет
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "source", "price"])  # Заголовки: временная метка, источник, цена

def log_arbitrage_opportunity(message):
    """Записывает сообщение об арбитраже в лог."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data/arbitrage_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

def log_price_data(source, price):
    """Записывает цену с временной меткой и источником в CSV."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, source, price])