numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if not numbers:
    print("Нет данных")
else:
    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / count
    print("Количество:", count)
    print("Сумма:", total)
    print("Минимум:", minimum)
    print("Максимум:", maximum)
    print(f"Среднее: {average:.2f}")
