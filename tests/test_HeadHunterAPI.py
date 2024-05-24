from abc import ABC

from src.HeadHunterAPI import Parser, HeadHunterAPI


def test_issubclass():
    assert issubclass(HeadHunterAPI, ABC)
    assert issubclass(HeadHunterAPI, Parser)


def test_get_vacancy_from_api(fixture_class_get_hh_valid, fixture_class_get_hh_negative):
    assert len(fixture_class_get_hh_valid) > 0
    assert fixture_class_get_hh_negative == []

