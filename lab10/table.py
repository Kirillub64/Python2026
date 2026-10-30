def row_sums(matrix):
    """Список сумм строк."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Список сумм столбцов."""
    if not matrix:
        return []
    columns = len(matrix[0])
    return [
        sum(matrix[row][col] for row in range(len(matrix)))
        for col in range(columns)
    ]
