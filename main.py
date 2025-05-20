import json

from src.classes import HH
from src.vacancy import Vacancy
from src.json_saver import JSONSaver

print("Введите ключевое слово для поиска вакансий")

while True:



hh = HH()
json_saver = JSONSaver()        #Создали экземпляр класса
vacancies = hh.load_vacancies('python')     # должно быть не python, а то, что вводит пользователь
json_saver.save_vacancies(vacancies)

# vac_ex = []
# for vacancy in vacancies:
#     vac_ex.append(Vacancy(**vacancy))

# for vacancy in vacancies:
#     # Если vacancy это строка в формате JSON, преобразуем её в словарь
#     if isinstance(vacancy, str):
#         try:
#             vacancy_dict = json.loads(vacancy)
#             vac_ex.append(Vacancy(**vacancy_dict))
#         except json.JSONDecodeError:
#             print(f'Ошибка при разборе данных вакансии: {vacancy}')
#             continue
#     # Если vacancy уже словарь, используем как есть
#     elif isinstance(vacancy, dict):
#         vac_ex.append(Vacancy(**vacancy))
#     else:
#         print(f"Неподдерживаемый формат данных вакансии: {type(vacancy)}")


# for vac in vac_ex:
#     print(vac)
#     print("------------------")

for vac in json_saver.get_vacancies():
    print(vac)
    print("------------------")