from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API HeadHunter"""

    @abstractmethod
    def _connect(self) -> dict:
        """Абстрактный метод соединения с API"""
        pass  # pragma: no cover

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict]:
        """Абстрактный метод для получения вакансий"""
        pass  # pragma: no cover


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        """Конструктор инициализирует объект класса HeadHunterAPI"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "", "page": 0, "per_page": 50}

    def _connect(self) -> dict:
        """Метод соединения с API HeadHunter"""
        response = requests.get(self.__url, params=self.__params)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError

    def load_vacancies(self, keyword: str) -> list[dict]:
        """Метод получения вакансий"""
        self.__params["text"] = keyword
        all_vacancies = []
        while self.__params["page"] < 3:
            vacancies = self._connect()["items"]
            all_vacancies.extend(self.filter_vacancy(vacancies))
            self.__params["page"] += 1
        return all_vacancies

    @staticmethod
    def filter_vacancy(vacancies: list[dict]) -> list[dict]:
        """Фильтрует и преобразует список вакансий в нужный формат"""
        all_vacancies = []
        for vacancy in vacancies:
            all_vacancies.append(
                {
                    "name": vacancy["name"],
                    "url": vacancy["alternate_url"],
                    "salary": vacancy["salary"],
                    "description": vacancy["snippet"]["requirement"],
                    "schedule": vacancy["schedule"]["name"],
                    "experience": vacancy["experience"]["name"],
                }
            )
        return all_vacancies
