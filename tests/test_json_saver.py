import json
import os

import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def test_save_vacancies(json_saver: JSONSaver, sample_vacancies: list[dict], test_file_path: str) -> None:
    """Тест сохранения вакансий в файл"""
    json_saver.save_vacancies(sample_vacancies)

    # Проверяем, что файл создан
    assert os.path.exists(test_file_path)

    # Проверяем содержимое файла
    with open(test_file_path, "r", encoding="utf-8") as file:
        saved_data = json.load(file)
    assert len(saved_data) == len(sample_vacancies)
    assert saved_data[0]["name"] == sample_vacancies[0]["name"]


def test_get_vacancies(json_saver: JSONSaver, sample_vacancies: list[dict]) -> None:
    """Тест получения вакансий из файла"""
    # Сначала сохраняем данные
    json_saver.save_vacancies(sample_vacancies)

    # Получаем вакансии
    vacancies = json_saver.get_vacancies()

    # Проверяем результат
    assert len(vacancies) == len(sample_vacancies)
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].name == sample_vacancies[0]["name"]
    assert vacancies[0].salary_from == sample_vacancies[0]["salary"]["from"]


def test_delete_vacancies(json_saver: JSONSaver, sample_vacancies: list[dict], test_file_path: str) -> None:
    """Тест удаления вакансий"""
    # Сначала сохраняем данные
    json_saver.save_vacancies(sample_vacancies)

    # Удаляем вакансии
    json_saver.delete_vacancies()

    # Проверяем, что файл пустой
    assert os.path.getsize(test_file_path) == 0


def test_file_not_found(tmp_path: str) -> None:
    """Тест обработки отсутствующего файла"""
    non_existent_path = str(tmp_path / "non_existent.json")
    saver = JSONSaver(path=non_existent_path)

    with pytest.raises(FileNotFoundError):
        saver.get_vacancies()


def test_invalid_json_format(json_saver: JSONSaver, test_file_path: str) -> None:
    """Тест обработки некорректного JSON"""
    # Создаем файл с некорректным JSON
    with open(test_file_path, "w", encoding="utf-8") as file:
        file.write('{"invalid": "json"')

    with pytest.raises(json.JSONDecodeError):
        json_saver.get_vacancies()


def test_save_empty_vacancies_list(json_saver: JSONSaver) -> None:
    """Тест сохранения пустого списка вакансий"""
    json_saver.save_vacancies([])
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 0


def test_invalid_vacancy_data(json_saver: JSONSaver, test_file_path: str) -> None:
    """Тест обработки некорректных данных вакансии"""
    invalid_data = [{"invalid_field": "value"}]  # Отсутствуют обязательные поля

    json_saver.save_vacancies(invalid_data)

    with pytest.raises(TypeError):
        json_saver.get_vacancies()
