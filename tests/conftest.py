from pytest import fixture

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