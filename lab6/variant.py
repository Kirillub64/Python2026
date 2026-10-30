numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if abs(number) % 10 == 2:
        selected.append(number)

count = len(selected)
total = sum(selected)
sorted_copy = sorted(selected)

print("Список:", selected)
print("Количество:", count)
print("Сумма:", total)
print("Отсортированная копия:", sorted_copy)
