from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.func import (filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies,
                      check_top_n)


def user_interaction():
    search_query = input("Введите поисковый запрос для поиска вакансий: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    check_top_n(top_n)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите желаемую зарплату: ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies, int(salary_range.split("-")[1]))
    print(vacancies_list)
    print(filter_words)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    print(filtered_vacancies)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    print(ranged_vacancies)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    print(sorted_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
