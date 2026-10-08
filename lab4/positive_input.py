n = int(input("Введите n (n >= 0): "))

count = 0        # счётчик подходящих чисел
total_sum = 0    # накопитель суммы подходящих чисел

for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))

    
    if abs(num) % 10 == 2:
        count += 1
        total_sum += num

print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
