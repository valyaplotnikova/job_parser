from src.Vacancy import Vacancy
from src.func import get_user_vacancies, filter_vacancies, sort_vacancies, get_salary_range_vacancies


def test_get_user_vacancies(fixture_vacancies_list):
    assert isinstance(get_user_vacancies(fixture_vacancies_list)[0], Vacancy) == True


def test_filter_vacancies(fixture_vacancy):
    assert len(filter_vacancies(fixture_vacancy, ['pазрабатывать'])) == 1
    assert len(filter_vacancies(fixture_vacancy, ['писать'])) == 2

def test_sort_vacancies(fixture_vacancy):
    assert sort_vacancies(fixture_vacancy)[0].salary_to == 60000


def test_get_salary_range_vacancies(fixture_vacancy):
    assert len(get_salary_range_vacancies(fixture_vacancy, 20000)) == 1
    assert len(get_salary_range_vacancies(fixture_vacancy, 50000)) == 2
