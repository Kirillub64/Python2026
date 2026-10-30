def row_sums(matrix):
    """Список сумм строк. Для [] — []."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Список сумм столбцов. Для [] — []."""
    if not matrix:
        return []
    columns = len(matrix[0])
    return [sum(matrix[row][col] for row in range(len(matrix)))
            for col in range(columns)]


def diagonal_pattern(size):
    """Квадратная таблица: диагональ 0, выше 1, ниже 2."""
    matrix = []
    for row in range(size):
        new_row = []
        for col in range(size):
            if row == col:
                new_row.append(0)
            elif row < col:
                new_row.append(1)
            else:
                new_row.append(2)
        matrix.append(new_row)
    return matrix


def transform(matrix):
    """Вариант 15: ненулевые элементы заменить знаком (1 или -1)."""
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if value > 0:
                new_row.append(1)
            elif value < 0:
                new_row.append(-1)
            else:
                new_row.append(0)
        result.append(new_row)
    return result
