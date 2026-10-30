from table import row_sums, column_sums, diagonal_pattern, transform


def read_matrix():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    matrix = read_matrix()
    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    size = int(input("Положительный размер узора: "))
    pattern = diagonal_pattern(size)
    print("Диагональный узор:")
    print_matrix(pattern)

    new_matrix = transform(matrix)
    print("Исходная таблица:")
    print_matrix(matrix)
    print("Новая таблица (вариант 15):")
    print_matrix(new_matrix)


if __name__ == "__main__":
    main()
