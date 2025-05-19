from abc import ABC, abstractmethod
import requests

class AbstractAPI(ABC):
    """Абстрактный класс для работы с API HeadHunter"""
    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(AbstractAPI):
    """Класс для работы с API HeadHunter"""

    # def __init__(self, file_worker):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'text': '', 'page': 0, 'per_page': 50}
        # self.headers = {'User-Agent': 'HH-User-Agent'}
        # self.vacancies = []
        # super().__init__(file_worker)


    def _connect(self):
        """Метод соединения с API HeadHunter"""
        # response = requests.get(self.__url, headers=self.headers, params=self.__params)
        response = requests.get(self.__url, params=self.__params)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError


    # def load_vacancies(self, keyword):
    #     """Метод получения вакансий"""
    #     self.__params['text'] = keyword
    #     vacancies = self._connect()['items']
    #     return vacancies

    def load_vacancies(self, keyword):
        """Метод получения вакансий"""
        self.__params['text'] = keyword
        all_vacancies = []
        while self.__params['page'] < 5:
            vacancies = self._connect()['items']
            all_vacancies.extend(self.filter_vacancy(vacancies))
            self.__params['page'] += 1
        return all_vacancies

    # def load_vacancies(self, keyword):
    #     """Метод получения вакансий"""
    #     self.params['text'] = keyword
    #     while self.params.get('page') != 20:
    #         response = requests.get(self.url, headers=self.headers, params=self.params)
    #         vacancies = response.json()['items']
    #         self.vacancies.extend(vacancies)
    #         self.params['page'] += 1

    @staticmethod
    def filter_vacancy(vacancies):
        all_vacancies = []
        for vacancy in vacancies:
            vacancy = {"name": vacancy["name"], "url": vacancy["alternate_url"], "salary": vacancy["salary"],
                    "description": vacancy["snippet"]["requirement"], "schedule": vacancy["schedule"]["name"],
                       "experience": vacancy["experience"]["name"]}
            all_vacancies.append(vacancy)
        return all_vacancies

# hh = HH()
# print(hh.load_vacancies('python')[0])
