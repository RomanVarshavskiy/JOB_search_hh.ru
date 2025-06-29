import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class JSONAbstract(ABC):
    """Абстрактный класс для работы с JSON-файлами вакансий"""

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        """Абстрактный метод для получения вакансий из источника данных"""
        pass  # pragma: no cover

    @abstractmethod
    def save_vacancies(self, vacancies: list[dict]) -> None:
        """Абстрактный метод для сохранения списка вакансий"""
        pass  # pragma: no cover

    @abstractmethod
    def delete_vacancies(self) -> None:
        """Абстрактный метод для удаления сохраненных вакансий"""
        pass  # pragma: no cover


class JSONSaver(JSONAbstract):
    """Класс для работы с вакансиями в JSON-файле"""

    def __init__(self, path: str = "data/vacancies.json") -> None:
        """Конструктор инициализирует объект JSONSaver"""
        self.__path = path

    def get_vacancies(self) -> list[Vacancy]:
        """Читает вакансии из JSON-файла и преобразует их в объекты Vacancy"""
        with open(self.__path, "r", encoding="utf-8") as file:
            data = json.load(file)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies

    def save_vacancies(self, vacancies: list[dict]) -> None:
        """Сохраняет список вакансий в JSON-файл"""
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self) -> None:
        """Очищает файл с вакансиями, удаляя все сохраненные данные"""
        open(self.__path, "w").close()
