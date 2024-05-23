import json
import os
from src.HeadHunterAPI import HeadHunterAPI


class JSONSaver:
    def save_to_file(self, vacancies, filename="vacancies.json", directory="data"):
        full_path = os.path.join("..", directory, filename)  # Путь к файлу

        for vacancion in vacancies:
            with open(full_path, 'w', encoding='utf-8') as file:
                json.dump(vacancion, file, indent=2, ensure_ascii=False)

    def read_to_file(self, filename="vacancies.json", directory="data"):
        full_path = os.path.join("..", directory, filename)  # Путь к файлу

        with open(full_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)


    def del_to_file(self, filename="vacancies.json", directory="data"):
        full_path = os.path.join("..", directory, filename)  # Путь к файлу
        with open(full_path, 'w', encoding='utf-8') as file:
            json.dump("", file, indent=2, ensure_ascii=False)

