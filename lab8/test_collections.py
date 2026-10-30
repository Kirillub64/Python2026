from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
)

# --- word_counts ---
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}

# --- common_topics / all_topics ---
assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]

# один из списков пуст
assert common_topics([], ["python", "sql"]) == []
assert all_topics([], ["python", "sql"]) == ["python", "sql"]

# --- вариант 15: фотоколлекция ---
records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}

# исходные записи не изменились
before = [record.copy() for record in records]
totals_by_category(records)
titles_in_category(records, "основное")
assert records == before

print("Все проверки пройдены")
