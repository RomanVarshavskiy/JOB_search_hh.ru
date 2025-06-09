from src.vacancy import Vacancy


def print_vacancies(vacancies: list[Vacancy]) -> None:
    for vacancy in vacancies:
        print(vacancy)


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    return sorted(vacancies)


def get_top_vacancies(vacancies: list[Vacancy], top: int) -> list[Vacancy]:
    return vacancies[:top]


def filter_vacancies(vacancies: list[Vacancy], keywords: list[str]) -> list[Vacancy]:
    """Фильтрует список вакансий по ключевым словам в описании"""
    if not keywords:  # Проверка на пустой список ключевых слов
        return []

    filtered_vacancies = []
    for vacancy in vacancies:
        description_lower = vacancy.description.lower()
        # Проверяем наличие всех ключевых слов в описании
        if all(keyword in description_lower for keyword in keywords):
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Фильтрует список вакансий по диапазону зарплат"""
    ranged_vacancies = []

    try:
        # Очищаем строку от пробелов и разделяем по дефису
        parts = [x.strip() for x in salary_range.split("-")]
        if len(parts) != 2:
            raise ValueError("Неверный формат диапазона зарплат")

        min_salary = int(parts[0])
        max_salary = int(parts[1])

        for vacancy in vacancies:
            if (
                vacancy.salary_from is not None
                and vacancy.salary_to is not None
                and vacancy.salary_from >= min_salary
                and vacancy.salary_to <= max_salary
            ):
                ranged_vacancies.append(vacancy)

    except (ValueError, IndexError) as e:
        print(f"Ошибка при обработке диапазона зарплат: {e}")
        print("Используйте формат: минимум-максимум (например: 100000-150000)")
        return []

    return ranged_vacancies
