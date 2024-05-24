class Vacancy:
    """
       Инициализация вакансии с заданными атрибутами
       """

    name: str  # Название вакансии
    url: str  # URL страницы вакансии
    salary_from: int  # Зарплата от предложенная за работу
    salary_to: int  # Зарплата до предложенная за работу
    snippet: str  # требования

    def __init__(self, name, url, salary_from, salary_to, snippet):
        self.name = name
        self.url = url
        self.salary_to = salary_to if salary_to is not None else 0
        self.salary_from = salary_from if salary_from is not None else 0
        self.snippet = snippet

    def __str__(self):
        """
        Строковое представление объекта
        """
        return (f'Название вакансии: {self.name} \n'
                f'Заработная плата: {self.salary_from} - {self.salary_to} \n'
                f'Требования: {self.snippet} \n'
                f'Ссылка на вакансию: {self.url}\n')

    def __repr__(self):
        """
        Официальное строковое представление объекта
        """
        return (f'Название вакансии: {self.name} \n'
                f'Заработная плата: {self.salary_from} - {self.salary_to} \n'
                f'Требования: {self.snippet} \n'
                f'Ссылка на вакансию: {self.url}\n')

    def __gt__(self, other):
        """
        Определение поведения для оператора '>'. Сравнивает вакансии по зарплате
        """
        if self.salary_to > other.salary_to:
            return True

