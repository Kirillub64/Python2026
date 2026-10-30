from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix, selected_sum


def expect_value_error(text, message):
    with TemporaryDirectory() as directory:
        path = Path(directory) / "matrix.txt"
        path.write_text(text, encoding="utf-8")
        try:
            read_matrix(path)
        except ValueError:
            pass
        else:
            assert False, message


# корректное чтение
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

# 1×1 и значение 0
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]

# пустой файл
expect_value_error("", "Пустой файл должен давать ValueError")

# заголовок 0 3
expect_value_error("0 3\n", "Нулевой размер должен давать ValueError")

# заголовок 1 2, строка 1
expect_value_error("1 2\n1\n", "Недостаток чисел в строке")

# заголовок 1 2, строка 1 x
expect_value_error("1 2\n1 x\n", "Нечисловая ячейка")

# заголовок 1 1, две строки данных
expect_value_error("1 1\n1\n2\n", "Лишние строки данных")

# отсутствующий файл
with TemporaryDirectory() as directory:
    missing = Path(directory) / "no_such.txt"
    try:
        read_matrix(missing)
    except FileNotFoundError:
        pass
    else:
        assert False, "Отсутствующий файл должен давать FileNotFoundError"

# вариант 15
assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 4
assert selected_sum([[7]]) == 7
assert selected_sum([[1, 2], [3, 4]]) == 1 + 2 + 4  # индексы (0,0),(0,1),(1,1)

print("Все проверки пройдены")
