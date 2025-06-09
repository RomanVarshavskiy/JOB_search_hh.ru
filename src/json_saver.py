import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class JSONAbstract(ABC):

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass  # pragma: no cover

    @abstractmethod
    def save_vacancies(self, vacancies: list[dict]) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def delete_vacancies(self) -> None:
        pass  # pragma: no cover


class JSONSaver(JSONAbstract):

    def __init__(self, path: str = "data/vacancies.json") -> None:
        self.__path = path

    def get_vacancies(self) -> list[Vacancy]:
        with open(self.__path, "r", encoding="utf-8") as file:
            data = json.load(file)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies

    def save_vacancies(self, vacancies: list[dict]) -> None:
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self) -> None:
        open(self.__path, "w").close()
