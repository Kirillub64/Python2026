def read_matrix(path):
    """Прочитать матрицу из файла. При ошибке формата — ValueError."""
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # убираем один допустимый перевод строки в конце
    if lines and lines[-1].strip() == "":
        lines.pop()

    if not lines:
        raise ValueError("Файл пуст")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось два числа — строки и столбцы")

    try:
        rows, cols = int(header[0]), int(header[1])
    except ValueError:
        raise ValueError("Строка 1: размеры должны быть целыми числами")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: размеры должны быть положительными")

    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(
            f"Ожидалось {rows} строк данных, получено {len(data_lines)}"
        )

    matrix = []
    for index, line in enumerate(data_lines, start=2):
        parts = line.split()
        if len(parts) != cols:
            raise ValueError(
                f"Строка {index}: ожидалось {cols} чисел, получено {len(parts)}"
            )
        try:
            row = [int(part) for part in parts]
        except ValueError:
            raise ValueError(f"Строка {index}: все ячейки должны быть целыми")
        matrix.append(row)

    return matrix


def selected_sum(matrix):
    """Вариант 15: сумма элементов с чётной суммой индексов (i + j) % 2 == 0."""
    total = 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if (i + j) % 2 == 0:
                total += value
    return total
