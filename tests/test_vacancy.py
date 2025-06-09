import pytest

from src.vacancy import Vacancy


def test_vacancy_initialization(sample_vacancy: Vacancy) -> None:
    """Тест корректной инициализации объекта и присвоения всех атрибутов"""
    assert sample_vacancy.name == "Python Developer"
    assert sample_vacancy.url == "https://example.com/job/123"
    assert sample_vacancy.salary_from == 100000
    assert sample_vacancy.salary_to == 150000
    assert sample_vacancy.description == "Python developer position"
    assert sample_vacancy.schedule == "Полный день"
    assert sample_vacancy.experience == "От 3 до 6 лет"


def test_salary_validation_empty() -> None:
    """Тест обработки пустой зарплаты"""
    vacancy = Vacancy(name="Test", url="test.com", salary=None, description="Test", schedule="Test", experience="Test")
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_salary_validation_partial() -> None:
    """Тест обработки частично заполненной зарплаты"""
    vacancy = Vacancy(
        name="Test",
        url="test.com",
        salary={"from": 100000},  # только from
        description="Test",
        schedule="Test",
        experience="Test",
    )
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 0


def test_vacancy_comparison() -> None:
    """Тест сравнения вакансий по зарплате"""
    vacancy1 = Vacancy(
        name="Test1", url="test1.com", salary={"from": 100000}, description="Test1", schedule="Test", experience="Test"
    )
    vacancy2 = Vacancy(
        name="Test2", url="test2.com", salary={"from": 200000}, description="Test2", schedule="Test", experience="Test"
    )
    assert vacancy1 < vacancy2


def test_vacancy_str_representation(sample_vacancy: Vacancy) -> None:
    """Тест строкового представления вакансии"""
    vacancy_str = str(sample_vacancy)
    assert "Python Developer" in vacancy_str
    assert "https://example.com/job/123" in vacancy_str
    assert "100000" in vacancy_str
    assert "150000" in vacancy_str
    assert "Python developer position" in vacancy_str


def test_vacancy_slots() -> None:
    """Тест наличия всех необходимых атрибутов в __slots__"""
    expected_slots = {"name", "url", "salary", "description", "schedule", "experience", "salary_from", "salary_to"}
    assert set(Vacancy.__slots__) == expected_slots


def test_invalid_vacancy_creation() -> None:
    """Тест создания вакансии с отсутствующими обязательными параметрами"""
    with pytest.raises(TypeError):
        Vacancy()  # без параметров
