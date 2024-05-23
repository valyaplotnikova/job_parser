def filter_vacancies(vacancies_list, filter_words):
    filter_vacancies_list = [vac for vac in vacancies_list if any(word in filter_words for word in vacancies_list)]
    if len(filter_vacancies_list) == 0:
        print('Ключевых слов не найдено. Работаем со всеми вакансиями')
        return vacancies_list
    return filter_vacancies_list


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    ranged_vacancies = []
    for vacancy in filtered_vacancies:
        print(int(vacancy.salary_from()))
        if int(vacancy.salary_to()) >= int(salary_range.split("-")[1]):
            ranged_vacancies.append(vacancy)

    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    return ranged_vacancies.sort()


def get_top_vacancies(sorted_vacancies, top_n):
    if len(sorted_vacancies) > top_n:
        return sorted_vacancies[:top_n]
    else:
        return sorted_vacancies


def print_vacancies(top_vacancies):
    print(top_vacancies)

def check_top_n(n):
    if n <= 0:
        raise ValueError("Введите корректное число")
    elif not isinstance(n, int):
        raise ValueError("Введите число")
    else:
        return n
