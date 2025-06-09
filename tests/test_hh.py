from unittest.mock import patch

from src.classes import HeadHunterAPI

@patch("requests.get")
def test_hh_class(mock_get, vacancies):
    hh = HeadHunterAPI()
    hh.load_vacancies("test")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"items": vacancies}
    data = hh.load_vacancies("test")
    assert len(data) == 25
    mock_get.assert_called()