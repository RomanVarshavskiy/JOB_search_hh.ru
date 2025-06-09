import pytest
from unittest.mock import Mock, patch
from src.classes import HeadHunterAPI

def test_init(hh_api):
    """Тест инициализации класса"""
    assert hh_api._HeadHunterAPI__url == 'https://api.hh.ru/vacancies'
    assert hh_api._HeadHunterAPI__params == {'text': '', 'page': 0, 'per_page': 50}

@patch('requests.get')
def test_connect_success(mock_get, hh_api, mock_vacancy_response):
    """Тест успешного подключения к API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_vacancy_response
    mock_get.return_value = mock_response

    response = hh_api._connect()
    assert response == mock_vacancy_response
    mock_get.assert_called_once()

@patch('requests.get')
def test_connect_failure(mock_get, hh_api):
    """Тест неудачного подключения к API"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    with pytest.raises(ValueError):
        hh_api._connect()

@patch('requests.get')
def test_load_vacancies(mock_get, hh_api, mock_vacancy_response):
    """Тест загрузки вакансий"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_vacancy_response
    mock_get.return_value = mock_response

    vacancies = hh_api.load_vacancies("python")

    assert len(vacancies) == 3  # 3 страницы по одной вакансии
    assert all(isinstance(vacancy, dict) for vacancy in vacancies)
    assert mock_get.call_count == 3  # Проверяем, что было 3 запроса

def test_filter_vacancy(hh_api, mock_vacancy_response):
    """Тест фильтрации вакансий"""
    filtered = hh_api.filter_vacancy(mock_vacancy_response["items"])

    assert len(filtered) == 1
    vacancy = filtered[0]
    assert vacancy["name"] == "Python Developer"
    assert vacancy["url"] == "https://hh.ru/vacancy/123"
    assert vacancy["salary"] == {"from": 100000, "to": 150000}
    assert vacancy["description"] == "Python, Django, SQL"
    assert vacancy["schedule"] == "Полный день"
    assert vacancy["experience"] == "От 1 до 3 лет"

@patch('requests.get')
def test_load_vacancies_empty_response(mock_get, hh_api):
    """Тест обработки пустого ответа от API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    vacancies = hh_api.load_vacancies("несуществующая_вакансия")
    assert len(vacancies) == 0

@patch('requests.get')
def test_load_vacancies_invalid_response(mock_get, hh_api):
    """Тест обработки некорректного ответа от API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"invalid_data": "value"}]}
    mock_get.return_value = mock_response

    with pytest.raises(KeyError):
        hh_api.load_vacancies("python")

def test_filter_vacancy_empty_list(hh_api):
    """Тест фильтрации пустого списка вакансий"""
    filtered = hh_api.filter_vacancy([])
    assert len(filtered) == 0

def test_abstract_class_instantiation():
    """Тест невозможности создания экземпляра абстрактного класса"""
    from src.classes import AbstractAPI

    with pytest.raises(TypeError):
        AbstractAPI()
