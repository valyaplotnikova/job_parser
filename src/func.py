from src.Vacancy import Vacancy


def get_user_vacancies(vacancies_list):
    user_vacancies = []
    for vacancy in vacancies_list:
        name = vacancy['name']
        url = vacancy['url']
        snippet = vacancy["snippet"]['requirement']
        salary_from = None
        salary_to = None
        if vacancy['salary'] is None:
            salary_from = 0
            salary_to = 0
        elif not vacancy['salary']['from'] and vacancy['salary']['to']:
            salary_from = vacancy['salary']['to']
            salary_to = vacancy['salary']['to']
        elif not vacancy['salary']['to'] and vacancy['salary']['from']:
            salary_from = vacancy['salary']['from']
            salary_to = vacancy['salary']['from']

        user_vacancies.append(Vacancy(name, url, salary_from, salary_to, snippet))
    return user_vacancies


def filter_vacancies(vacancies_list, filter_words):
    filter_vacancies_list = []
    for vacancy in vacancies_list:
        if vacancy.snippet is not None:
            if any(map(lambda x: x in vacancy.snippet, filter_words)):
                filter_vacancies_list.append(vacancy)
    if len(filter_vacancies_list) == 0:
        print('Ключевых слов не найдено. Работаем со всеми вакансиями')
        return vacancies_list
    else:
        print(f"По заданным ключевым словам нашлось {len(filter_vacancies_list)} вакансий")
    return filter_vacancies_list


def sort_vacancies(ranged_vacancies):
    sort_vacancies_list = sorted(ranged_vacancies, key=lambda x: x.salary_to, reverse=True)
    return sort_vacancies_list


def get_top_vacancies(sorted_vacancies, top_n):
    if len(sorted_vacancies) > top_n:
        return sorted_vacancies[:top_n]
    else:
        return sorted_vacancies


def print_vacancies(top_vacancies):
    print(top_vacancies)


def get_salary_range_vacancies(user_vacancies, salary_range):
    salary_range_vacancies = []
    for vacancy in user_vacancies:
        if vacancy.salary_from > int(salary_range):
            salary_range_vacancies.append(vacancy)
    if len(salary_range_vacancies) == 0:
        print('Подходящих вакансий не найдено')
        return user_vacancies
    else:
        print(f"По заданной заработной плате нашлось {len(salary_range_vacancies)} вакансий")
    return salary_range_vacancies
