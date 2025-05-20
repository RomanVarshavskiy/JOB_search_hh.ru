import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class JSONAbstract(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

class JSONSaver(JSONAbstract):

    def __init__(self, path="data/vacancies.json"):
        self.__path = path

    def get_vacancies(self) -> list[Vacancy]:
        with open(self.__path, "r", encoding="utf-8") as file:
            data = json.load(file)

        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies

    def save_vacancies(self, vacancies: list[dict]):
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self):
        open(self.__path, "w").close()