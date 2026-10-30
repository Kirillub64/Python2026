from functions import average, normalize_text, sum_digits, select_numbers

# --- sum_digits ---
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12

# --- average ---
assert average([]) is None
assert average([2, 4, 6]) == 4

# --- normalize_text ---
assert normalize_text(" ПРИВЕТ Мир ") == "привет мир"
assert normalize_text("   ") == ""

# --- select_numbers (вариант 15) ---
# контрольный список из задания: при пороге 2 → пусто
assert select_numbers([-5, 0, 2, 5], 2) == []

# пустой список → []
assert select_numbers([], 2) == []

# при пороге 0 совпадений нет
assert select_numbers([-5, 0, 2, 5], 0) == []

# строгие границы: при пороге 2 подходит только |n| = 3
assert select_numbers([3, -3, 2, 4, 1], 2) == [3, -3]

# повторы сохраняются, порядок исходный
assert select_numbers([3, 3, -3, 5], 2) == [3, 3, -3]

# исходный список не изменился
original = [-5, 0, 2, 5]
before = original.copy()
select_numbers(original, 2)
assert original == before

print("Все проверки пройдены")
