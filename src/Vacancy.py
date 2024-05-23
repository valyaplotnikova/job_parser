class Vacancy:
    """
       Инициализация вакансии с заданными атрибутами
       """

    title: str  # Название вакансии
    url: str  # URL страницы вакансии
    salary_to: int  # Зарплата от предложенная за работу
    salary_from: int  # Зарплата до предложенная за работу
    requirement: str  # требования
    list_vacancies = []  # список вакансий по запросу

    def __init__(self, name, url, salary_from, salary_to, snippet):
        self.name = name
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.snippet = snippet
        self.list_vacancies.append(self)

    def __str__(self):
        """
        Строковое представление объекта
        """
        return f'{self.name} {self.salary_from} - {self.salary_to} {self.snippet}'

    def __repr__(self):
        """
        Официальное строковое представление объекта
        """
        return f'{self.name}  {self.salary_from} - {self.salary_to} {self.snippet}'

    def __gt__(self, other):
        """
        Определение поведения для оператора '>'. Сравнивает вакансии по зарплате
        """
        return self.salary_to > other.salary_to

    @classmethod
    def cast_to_object_list(cls, list_vacancy, salary_from):
        """
        Получает список со словарями вакансий. Возвращает новый список с вакансиями
        """
        for vacancy in list_vacancy:
            name_vacancy = vacancy["name"]
            url = vacancy["alternate_url"]
            snippet = vacancy["snippet"]
            if vacancy["salary"] is None:
                pass
            elif vacancy["salary"]["to"] is not None and vacancy["salary"]["from"]:
                if vacancy["salary"]["from"] >= salary_from:
                    salary_from = vacancy["salary"]["from"]
                    salary_to = vacancy["salary"]["to"]

                    cls(name_vacancy, salary_from, salary_to, url, snippet)
                else:
                    continue
            else:
                continue
        return cls.list_vacancies
