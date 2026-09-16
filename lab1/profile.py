# Карточка студента (тестовая версия, данные вписаны)
surname = "Шепранов"
name = "Кирилл"
group = "УБ-64"
city = "Воронеж"
age = 18
subject = "Физкультура"
hours = 2

if not (1 <= age <= 120):
    print("Ошибка: возраст должен быть от 1 до 120")
    raise SystemExit
if hours < 0:
    print("Ошибка: часы не могут быть отрицательными")
    raise SystemExit

age_in_4_years = age + 4
hours_in_4_weeks = hours * 4
hours_per_day = hours_in_4_weeks / 7

print("=== Карточка студента ===")
print(f"Студент: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Любимый предмет: {subject}")
print(f"Часов подготовки в неделю: {hours:.2f}")
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Подготовка за 4 недели: {hours_in_4_weeks:.2f} ч")
print(f"Среднее время в день: {hours_per_day:.2f} ч")
