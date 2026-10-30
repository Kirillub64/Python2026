from pathlib import Path

from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums


def read_positive_integer():
    """Повторять ввод, пока не получено целое число > 0."""
    while True:
        raw = input("Введите положительное целое: ")
        try:
            value = int(raw)
        except ValueError:
            print("Это не целое число")
            continue
        if value <= 0:
            print("Число должно быть больше нуля")
            continue
        return value


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "matrix.txt"
    report = folder / "report.txt"

    try:
        matrix = read_matrix(source)
    except FileNotFoundError:
        print("Файл matrix.txt не найден")
        return
    except UnicodeError:
        print("Не удалось прочитать matrix.txt в кодировке UTF-8")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return
    except ValueError as error:
        print(f"Ошибка формата: {error}")
        return

    rows = row_sums(matrix)
    cols = column_sums(matrix)
    variant_result = selected_sum(matrix)

    # запись только после успешной проверки всех данных
    with open(report, "w", encoding="utf-8") as file:
        file.write("Суммы строк: " + " ".join(map(str, rows)) + "\n")
        file.write("Суммы столбцов: " + " ".join(map(str, cols)) + "\n")
        file.write(f"Результат варианта: {variant_result}\n")

    print("Отчёт записан в report.txt")


if __name__ == "__main__":
    main()
