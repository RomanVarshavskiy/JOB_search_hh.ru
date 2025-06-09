from src.classes import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


search_query = input("Введите ключевое слово для поиска вакансий в hh.ru: ")

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh = HeadHunterAPI()
json_saver = JSONSaver()
vacancies_list = hh.load_vacancies(search_query)
json_saver.save_vacancies(vacancies_list)

# Преобразование списка словарей в список объектов Vacancy
vacancy_objects = [Vacancy(**vacancy) for vacancy in vacancies_list]

def user_interaction():
    """Функция для взаимодействия с пользователем"""
    filter_words = input("Введите ключевое слово для фильтрации вакансий: ").lower().split()
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancy_objects, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
