# Учебная нагрузка
subj1 = "История"
cnt1 = 2
dur1 = 135

subj2 = "Физика"
cnt2 = 2
dur2 = 135

# Суммарная нагрузка: (2*135) + (2*135) = 540 мин = 9 ч
# Свободного времени поставим 12 часов в неделю
free_hours = 12

if cnt1 < 0 or cnt2 < 0:
    print("Ошибка: количество занятий не может быть отрицательным")
    raise SystemExit
if dur1 <= 0 or dur2 <= 0:
    print("Ошибка: длительность должна быть положительной")
    raise SystemExit

minutes1 = cnt1 * dur1
minutes2 = cnt2 * dur2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60

if free_hours < total_hours:
    print("Ошибка: доступного времени меньше суммарной нагрузки")
    raise SystemExit

free_left = free_hours - total_hours
four_weeks = total_hours * 4

print(f"{subj1}: {minutes1} мин")
print(f"{subj2}: {minutes2} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {free_left:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks:.2f} ч")
