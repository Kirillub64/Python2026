def sum_digits(number):
    """Вернуть сумму цифр модуля числа. Для нуля — 0."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    """Вернуть среднее списка или None, если список пуст."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вернуть числа, у которых порог < |число| < 2*порог (вариант 15)."""
    result = []
    for number in numbers:
        if threshold < abs(number) < 2 * threshold:
            result.append(number)
    return result
