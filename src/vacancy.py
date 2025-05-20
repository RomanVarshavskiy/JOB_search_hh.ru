class Vacancy:

    #__slots__ = ('id', 'title', 'company', 'salary', 'link')

    def __init__(self, name, url, salary, description, schedule, experience):
        self.name = name
        self.url = url
        self.description = description
        self.schedule = schedule
        self.experience = experience
        self.__validate_salary(salary)


    def __validate_salary(self, salary):
        """Метод присваивает значение salary, в зависимости от данных в словаре"""
        if not salary:      # Если ЗП не указана
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary.get('from') if salary.get('from') else 0
            self.salary_to = salary.get('to') if salary.get('to') else 0

    def __lt__(self, other):    # lt - сравнение знака "<"
        return self.salary_from < other.salary_from


    def __str__(self):
        return f"""Название вакансии: {self.name},
Ссылка: {self.url},
Зарплата: от {self.salary_from} до {self.salary_to} ,
Описание: {self.description},
Расписание: {self.schedule},
Опыт: {self.experience}
"""