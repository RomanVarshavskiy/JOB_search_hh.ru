class Vacancy:
    """Класс для представления вакансии"""

    __slots__ = ("name", "url", "salary", "description", "schedule", "experience", "salary_from", "salary_to")

    def __init__(self, name: str, url: str, salary: dict, description: str, schedule: str, experience: str) -> None:
        """Инициализирует объект вакансии"""
        self.name = name
        self.url = url
        self.description = description
        self.schedule = schedule
        self.experience = experience
        self.__validate_salary(salary)

    def __validate_salary(self, salary: dict) -> None:
        """Метод присваивает значение salary, в зависимости от данных в словаре"""
        if not salary:  # Если ЗП не указана
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary.get("from") if salary.get("from") else 0
            self.salary_to = salary.get("to") if salary.get("to") else 0

    def __lt__(self, other: "Vacancy") -> bool:  # lt - сравнение знака "<"
        """Сравнивает две вакансии по минимальной зарплате"""

        return self.salary_from < other.salary_from

    def __str__(self) -> str:
        """Возвращает строковое представление вакансии"""
        return f"""Название вакансии: {self.name},
Ссылка: {self.url},
Зарплата: от {self.salary_from} до {self.salary_to} ,
Описание: {self.description},
Расписание: {self.schedule},
Опыт: {self.experience}
"""
