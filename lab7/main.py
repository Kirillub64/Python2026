from functions import sum_digits, average, normalize_text, select_numbers


def main():
    number = int(input("Целое число: "))
    print("Сумма цифр:", sum_digits(number))

    parts = input("Числа через пробел: ").split()
    numbers = [int(part) for part in parts]
    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print("Среднее:", avg)

    text = input("Текст: ")
    print("Нормализованный текст:", normalize_text(text))

    threshold = int(input("Порог: "))
    print("Выборка по варианту 15:", select_numbers(numbers, threshold))


if __name__ == "__main__":
    main()
