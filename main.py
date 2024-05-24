from src.HeadHunterAPI import HeadHunterAPI
from src.func import (filter_vacancies, sort_vacancies, get_top_vacancies,
                      print_vacancies, get_user_vacancies, get_salary_range_vacancies)


def user_interaction():
    search_query = input("Введите поисковый запрос для поиска вакансий: ")
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    user_vacancies = get_user_vacancies(hh_vacancies)
    print(f"Всего нашлось {len(user_vacancies)}")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    filtered_vacancies = filter_vacancies(user_vacancies, filter_words)
    salary_range = input("Введите желаемую зарплату: ")
    salary_range_vacancies = get_salary_range_vacancies(filtered_vacancies, salary_range)
    user_answer = input("Хотите получить список подходящих вакансий?  ").lower()
    if user_answer == "yes" or user_answer == "да":
        print(salary_range_vacancies)
    try:
        top_n = int(input('Введите количество вакансий для отображения по убыванию зарплаты: '))
        if top_n <= 0:
            raise ValueError
    except ValueError:
        print('Получено некорректное значение. Будут выданы все результаты:')
        top_n = None
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
