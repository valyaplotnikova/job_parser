import json
import os
from abc import ABC, abstractmethod


class FileSaver(ABC):
    @abstractmethod
    def save_to_file(self, *args, **kwargs):
        pass

    def read_to_file(self, *args, **kwargs):
        pass

    def del_to_file(self, *args, **kwargs):
        pass


class JSONSaver(FileSaver):

    @staticmethod
    def save_to_file(vacancies, filename="vacancies.json", directory="data"):
        full_path = os.path.join("..", directory, filename)  # Путь к файлу
        with open(full_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def read_to_file(self, filename="vacancies.json", directory="data"):
        full_path = os.path.join("..", directory, filename)  # Путь к файлу

        with open(full_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def del_to_file(self, filename="vacancies.json", directory="data"):
        full_path = os.path.join("..", directory, filename)  # Путь к файлу
        with open(full_path, 'w', encoding='utf-8') as file:
            json.dump("", file, indent=2, ensure_ascii=False)
