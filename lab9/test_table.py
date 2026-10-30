from table import row_sums, column_sums, diagonal_pattern, transform

# --- суммы строк и столбцов ---
assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]

assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

assert row_sums([]) == []
assert column_sums([]) == []

# --- диагональный узор ---
assert diagonal_pattern(1) == [[0]]
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]

# --- вариант 15: ненулевые заменить знаком ---
assert transform([[-2, 0, 3], [4, -5, 6]]) == [
    [-1, 0, 1],
    [1, -1, 1],
]
assert transform([]) == []

# --- независимость результата от исходной матрицы ---
original = [[-2, 0, 3], [4, -5, 6]]
result = transform(original)
result[0][0] = 99
assert original == [[-2, 0, 3], [4, -5, 6]]

print("Все проверки пройдены")
