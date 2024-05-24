from abc import ABC

from src.JSONSaver import FileSaver, JSONSaver


def test_json_saver_issubclass():
    assert issubclass(JSONSaver, FileSaver)
    assert issubclass(FileSaver, ABC)


def test_save_to_file(fixture_class_json_saver):
    fixture_class_json_saver.save_to_file([{'name1': 'inform1'}])

    assert isinstance(fixture_class_json_saver.read_to_file(), list)


def test_read_to_file_and_delete(fixture_class_list):

    assert fixture_class_list.read_to_file() == [{'name1': 'inform1'}]

    fixture_class_list.del_to_file()
    assert fixture_class_list.read_to_file() == ""
