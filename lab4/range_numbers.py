n = int(input("Введите n (n >= 1): "))

total_sum = 0          # накопитель суммы
positive_count = 0     # счётчик положительных
max_value = None       # максимум (инициализируем None, чтобы поймать первое число)

for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))

    # 1. Накапливаем сумму
    total_sum += num

    # 2. Считаем положительные
    if num > 0:
        positive_count += 1

    # 3. Обновляем максимум
    if max_value is None or num > max_value:
        max_value = num

print(f"Сумма: {total_sum}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {max_value}")
