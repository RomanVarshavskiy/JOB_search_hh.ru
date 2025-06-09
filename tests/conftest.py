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
def vacancies():
    return [{
        "name": "QA Engineer / Тестировщик",
        "alternate_url": "https://hh.ru/vacancy/120769384",
        "salary": None,
        "snippet": {"requirement": "Знание TCP, HTTP/HTTPS, REST"},
        "schedule": "Полный день",
        "experience": "От 1 года до 3 лет"
    },
    {
        "name": "Инженер-тестировщик",
        "alternate_url": "https://hh.ru/vacancy/120812947",
        "salary": None,
        "snippet": {"requirement": "Будет плюсом если ваш опыт содержит: - Умение писать тестовые сценарии"},
        "schedule": "Полный день",
        "experience": "От 3 до 6 лет"
    },
    {
        "name": "Backend-разработчик (Python)",
        "alternate_url": "https://hh.ru/vacancy/120798907",
        "salary": {
            "from": 130000,
            "to": 160000,
            "currency": "RUR",
            "gross": True
        },
        "snippet": {"requirement": "Уверенный опыт работы с <highlighttext>Python</highlighttext>3, Django-Rest"},
        "schedule": "Полный день",
        "experience": "От 3 до 6 лет"
    },
    {
        "name": "Junior backend-разработчик",
        "alternate_url": "https://hh.ru/vacancy/120778647",
        "salary": {
            "from": 40000,
            "to": None,
            "currency": "RUR",
            "gross": True
        },
        "snippet": {"requirement": "Опыт работы с Go. Пройденный GoTour. Работа с git. Примеры проектов"},
        "schedule": "Полный день",
        "experience": "Нет опыта"
    },
    {
        "name": "Тестировщик QA",
        "alternate_url": "https://hh.ru/vacancy/120773498",
        "salary": {
            "from": 130000,
            "to": 170000,
            "currency": "RUR",
            "gross": False
        },
        "snippet": {"requirement": "Понимание принципов безопасной разработки. Умение анализировать требования"},
        "schedule": "Полный день",
        "experience": "От 1 года до 3 лет"
    }]

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