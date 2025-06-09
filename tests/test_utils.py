import pytest
from src.utils import (print_vacancies, sort_vacancies, get_top_vacancies,
                       filter_vacancies, get_vacancies_by_salary)
from src.vacancy import Vacancy


def test_print_vacancies(test_vacancies, capsys):
    """Тест функции print_vacancies"""
    print_vacancies(test_vacancies)
    captured = capsys.readouterr()

    # Проверяем, что что-то было выведено
    assert captured.out != ""

    # Проверяем, что названия всех вакансий присутствуют в выводе
    for vacancy in test_vacancies:
        assert vacancy.name in captured.out

    # Проверяем наличие основной информации для каждой вакансии
    output = captured.out.lower()
    assert "название вакансии" in output
    assert "ссылка" in output
    assert "зарплата" in output
    assert "описание" in output
    assert "расписание" in output
    assert "опыт" in output


def test_sort_vacancies(test_vacancies):
    """Тест функции sort_vacancies"""
    sorted_vacancies = sort_vacancies(test_vacancies)

    # Проверяем, что количество вакансий не изменилось
    assert len(sorted_vacancies) == len(test_vacancies)

    # Проверяем, что вакансии отсортированы по возрастанию зарплаты
    for i in range(len(sorted_vacancies) - 1):
        assert sorted_vacancies[i].salary_from <= sorted_vacancies[i + 1].salary_from


def test_get_top_vacancies(test_vacancies):
    """Тест функции get_top_vacancies"""
    # Тест получения двух верхних вакансий
    top_2 = get_top_vacancies(test_vacancies, 2)
    assert len(top_2) == 2
    assert top_2[0].name == test_vacancies[0].name
    assert top_2[1].name == test_vacancies[1].name

    # Тест с количеством больше, чем есть вакансий
    top_5 = get_top_vacancies(test_vacancies, 5)
    assert len(top_5) == len(test_vacancies)

    # Тест с нулевым количеством
    top_0 = get_top_vacancies(test_vacancies, 0)
    assert len(top_0) == 0


def test_filter_vacancies(test_vacancies):
    """Тест функции filter_vacancies"""
    # Тест фильтрации по одному ключевому слову
    python_vacancies = filter_vacancies(test_vacancies, ["python"])
    assert len(python_vacancies) == 2

    # Тест фильтрации по нескольким ключевым словам
    django_vacancies = filter_vacancies(test_vacancies, ["python", "django"])
    assert len(django_vacancies) == 1

    # Тест с несуществующим ключевым словом
    empty_result = filter_vacancies(test_vacancies, ["golang"])
    assert len(empty_result) == 0

    # Тест с пустым списком ключевых слов
    no_keywords = filter_vacancies(test_vacancies, [])
    assert len(no_keywords) == 0


def test_get_vacancies_by_salary(test_vacancies):
    """Тест функции get_vacancies_by_salary"""

    # Тест с корректным диапазоном зарплат
    filtered = get_vacancies_by_salary(test_vacancies, "100000-200000")
    assert len(filtered) == 1
    assert filtered[0].name == "Python Dev Middle"

    # Тест с другим диапазоном
    filtered = get_vacancies_by_salary(test_vacancies, "70000-130000")
    assert len(filtered) == 1
    assert filtered[0].name == "Python Dev Junior"

    # Тест с диапазоном, не включающим ни одну вакансию
    filtered = get_vacancies_by_salary(test_vacancies, "400000-500000")
    assert len(filtered) == 0

    # Тест с некорректным форматом диапазона
    filtered = get_vacancies_by_salary(test_vacancies, "100000")
    assert len(filtered) == 0

    # Тест с пустым списком вакансий
    filtered = get_vacancies_by_salary([], "100000-200000")
    assert len(filtered) == 0

    # Тест с некорректными значениями в диапазоне
    filtered = get_vacancies_by_salary(test_vacancies, "abc-def")
    assert len(filtered) == 0

    # Тест с пробелами в диапазоне
    filtered = get_vacancies_by_salary(test_vacancies, "100000 - 200000")
    assert len(filtered) == 1
    assert filtered[0].name == "Python Dev Middle"


@pytest.mark.parametrize("invalid_range", [
    "",  # пустая строка
    "100000",  # одно число
    "100000-",  # неполный диапазон
    "-100000",  # неполный диапазон
    "abc-def",  # нечисловые значения
    "100000-50000",  # мин больше макс
    "100000,200000",  # неверный разделитель
])
def test_get_vacancies_by_salary_invalid_input(test_vacancies, invalid_range):
    """Тест функции get_vacancies_by_salary с некорректными входными данными"""
    filtered = get_vacancies_by_salary(test_vacancies, invalid_range)
    assert len(filtered) == 0
