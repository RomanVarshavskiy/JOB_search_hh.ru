from pytest import fixture

from src.classes import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@fixture
def sample_vacancy():
    """Фикстура для создания тестового объекта вакансии"""
    return Vacancy(
        name="Python Developer",
        url="https://example.com/job/123",
        salary={"from": 100000, "to": 150000},
        description="Python developer position",
        schedule="Полный день",
        experience="От 3 до 6 лет"
    )

@fixture
def test_file_path(tmp_path):
    """Фикстура для создания временного пути к тестовому файлу"""
    return str(tmp_path / "test_vacancies.json")

@fixture
def json_saver(test_file_path):
    """Фикстура для создания экземпляра JSONSaver"""
    return JSONSaver(path=test_file_path)

@fixture
def sample_vacancies():
    """Фикстура с тестовыми данными вакансий"""
    return [
        {
            "name": "Python Developer",
            "url": "https://example.com/job/1",
            "salary": {"from": 100000, "to": 150000},
            "description": "Python position",
            "schedule": "Полный день",
            "experience": "От 3 до 6 лет"
        },
        {
            "name": "Java Developer",
            "url": "https://example.com/job/2",
            "salary": {"from": 120000, "to": 180000},
            "description": "Java position",
            "schedule": "Полный день",
            "experience": "От 1 до 3 лет"
        }
    ]

@fixture
def hh_api():
    """Фикстура для создания экземпляра API"""
    return HeadHunterAPI()

@fixture
def mock_vacancy_response():
    """Фикстура с тестовыми данными ответа API"""
    return {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/123",
                "salary": {
                    "from": 100000,
                    "to": 150000
                },
                "snippet": {
                    "requirement": "Python, Django, SQL"
                },
                "schedule": {
                    "name": "Полный день"
                },
                "experience": {
                    "name": "От 1 до 3 лет"
                }
            }
        ]
    }

@fixture
def test_vacancies():
    """Фикстура с тестовыми вакансиями"""
    return [
        Vacancy(
            name="Python Dev Junior",
            url="url1",
            salary={"from": 80000, "to": 120000},
            description="Python junior developer",
            schedule="full-time",
            experience="1-3"
        ),
        Vacancy(
            name="Python Dev Middle",
            url="url2",
            salary={"from": 150000, "to": 200000},
            description="Python middle developer, Django",
            schedule="full-time",
            experience="3-6"
        ),
        Vacancy(
            name="Java Dev Senior",
            url="url3",
            salary={"from": 200000, "to": 300000},
            description="Java senior developer",
            schedule="full-time",
            experience="6+"
        )
    ]