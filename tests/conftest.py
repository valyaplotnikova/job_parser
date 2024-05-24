import pytest

from src.HeadHunterAPI import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy


@pytest.fixture
def fixture_class_get_hh_valid():
    return HeadHunterAPI().get_vacancies('python')


@pytest.fixture
def fixture_class_get_hh_negative():
    return HeadHunterAPI().get_vacancies('1')


@pytest.fixture
def fixture_class_json_saver():
    return JSONSaver()


@pytest.fixture
def fixture_class_list():
    json_saver = JSONSaver()
    json_saver.save_to_file([{'name1': 'inform1'}])
    return json_saver


@pytest.fixture
def fixture_vacancies_list():
    vacancies_list = [{'id': '99938957', 'premium': False, 'name': 'Руководитель филиала', 'department': None,
                       'has_test': False, 'response_letter_required': False,
                       'area': {'id': '68', 'name': 'Омск', 'url': 'https://api.hh.ru/areas/68'},
                       'salary': None, 'type': {'id': 'open', 'name': 'Открытая'},
                       'address': None, 'response_url': None, 'sort_point_distance': None,
                       'published_at': '2024-05-23T11:41:05+0300', 'created_at': '2024-05-23T11:41:05+0300',
                       'archived': False,
                       'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=99938957',
                       'show_logo_in_search': None,
                       'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/99938957?host=hh.ru',
                       'alternate_url': 'https://hh.ru/vacancy/99938957', 'relations': [],
                       'employer': {'id': '851204', 'name': 'Торговый Дом Вертикаль',
                                    'url': 'https://api.hh.ru/employers/851204',
                                    'alternate_url': 'https://hh.ru/employer/851204',
                                    'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/990389.jpeg',
                                                  '240': 'https://img.hhcdn.ru/employer-logo/990390.jpeg',
                                                  'original': 'https://img.hhcdn.ru/employer-logo-original/128110.jpg'},
                                    'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=851204',
                                    'accredited_it_employer': False, 'trusted': True},
                       'snippet': {'requirement': 'Высшее специальное образование (коммерческое/экономическое/финансовое). '
                                                  'Опыт работы в 1С, CRM программах. Опыт работы от 3-х лет руководителем...',
                                   'responsibility': 'Организация развития филиала (продажи, склад, сервис). '
                                                     'Руководство и управление филиалом.'
                                                     ' <highlighttext>Разработка</highlighttext> '
                                                     'стратегических планов увеличения продаж. '
                                                     'Анализ текущих показателей продаж, планирование. '},
                       'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
                       'working_time_intervals': [], 'working_time_modes': [],
                       'accept_temporary': False, 'professional_roles': [{'id': '161', 'name': 'Руководитель филиала'}],
                       'accept_incomplete_resumes': False,
                       'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'},
                       'employment': {'id': 'full', 'name': 'Полная занятость'},
                       'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]
    return vacancies_list

@pytest.fixture
def fixture_vacancy():
    vacancies = []
    vacancy = Vacancy('Москва', 'https://api.hh.ru/areas/26',
                      50000, 60000, "Разрабатывать сайты")
    vacancy2 = Vacancy('Москва', 'https://api.hh.ru/areas/26',
                       10000, 40000, "Создавать контент")
    vacancies = [vacancy, vacancy2]
    return vacancies