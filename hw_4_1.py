def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total_salary = 0
            num_developers = 0

            for line in file:
                developer, salary_str = line.strip().split(",")
                salary = int(salary_str)
                total_salary += salary
                num_developers += 1
            average_salary = total_salary / num_developers
            return total_salary, average_salary
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдений.")
        return None


result = total_salary("salary_file.txt")

if result is not None:
    total, average = result
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
