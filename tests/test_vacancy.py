from src.Vacancy import Vacancy


def test_vacancy():
    vacancy = Vacancy('Москва', 'https://api.hh.ru/areas/26', 50000, 60000, "")
    vacancy2 = Vacancy('Москва', 'https://api.hh.ru/areas/26', 10000, 40000, "")

    result = vacancy > vacancy2
    assert result == True
