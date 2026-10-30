def word_counts(text):
    """Вернуть словарь «слово → количество» по правилам работы."""
    counts = {}
    for word in text.lower().split():
        clean = word.strip(".,!?;:")
        if clean == "":
            continue
        counts[clean] = counts.get(clean, 0) + 1
    return counts


def print_word_counts(counts):
    """Вывести пары «слово: количество» по алфавиту."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Отсортированный список общих тем."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Отсортированный список всех уникальных тем."""
    return sorted(set(first) | set(second))


def totals_by_category(records):
    """Словарь сумм amount по категориям (вариант 15: фотоколлекция)."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Названия записей указанной категории в исходном порядке."""
    result = []
    for record in records:
        if record["category"] == category:
            result.append(record["title"])
    return result


if __name__ == "__main__":
    # Задание 3: запись и пара
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False
    pair = (record["title"], record["hours"])
    name, hours = pair
    print("Пара:", name, hours)

    # Демонстрация word_counts
    print_word_counts(word_counts("Python, python! SQL"))

    # Демонстрация варианта 15 (фотоколлекция)
    records = [
        {"title": "Закат", "category": "пейзаж", "amount": 12},
        {"title": "Портрет", "category": "люди", "amount": 5},
        {"title": "Море", "category": "пейзаж", "amount": 8},
        {"title": "Улица", "category": "город", "amount": 3},
        {"title": "Лес", "category": "пейзаж", "amount": 6},
    ]
    print("Сводка:", totals_by_category(records))
    category = input("Категория для поиска: ")
    print("Названия:", titles_in_category(records, category))
