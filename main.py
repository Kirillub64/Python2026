import sys
from pathlib import Path
import logic
import storage

def main():
    base_dir = Path(__file__).resolve().parent
    data_file = base_dir / "data.json"

    try:
        records = storage.load_records(data_file)
        logic.validate_records(records)
    except Exception as e:
        print(f"Критическая ошибка при загрузке данных: {e}")
        sys.exit(1)

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показать записи")
        print("2. Добавить запись")
        print("3. Найти записи")
        print("4. Изменить статус")
        print("5. Удалить запись")
        print("6. Показать статистику")
        print("7. Сохранить данные")
        print("8. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            if not records:
                print("Нет записей.")
                continue
            for r in sorted(records, key=lambda x: x["id"]):
                status = "✔" if r["completed"] else "✘"
                print(f"[{r['id']}] {r['title']} | {r['category']} | {r['amount']} снимков | {status}")

        elif choice == "2":
            while True:
                title = input("Название: ").strip()
                if title: break
                print("Ошибка: название не может быть пустым.")
            while True:
                category = input("Категория: ").strip()
                if category: break
                print("Ошибка: категория не может быть пустой.")
            while True:
                try:
                    amount = int(input("Количество снимков: "))
                    if amount < 0: raise ValueError
                    break
                except ValueError:
                    print("Ошибка: нужно целое число >= 0.")
            new_rec = logic.add_record(records, title, category, amount)
            print(f"Добавлена запись с ID {new_rec['id']}")

        elif choice == "3":
            query = input("Введите подстроку для поиска: ").strip()
            try:
                found = logic.find_records(records, query)
                if not found:
                    print("Ничего не найдено.")
                else:
                    for r in found:
                        print(f"[{r['id']}] {r['title']} ({r['category']})")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            try:
                rid = int(input("Введите ID записи: "))
                status_input = input("Установить статус (1 - выполнено, 0 - не выполнено): ").strip()
                if status_input not in ("0", "1"):
                    print("Ошибка: введите 0 или 1.")
                    continue
                new_status = bool(int(status_input))
                if logic.set_completed(records, rid, new_status):
                    print("Статус изменен.")
                else:
                    print("Запись с таким ID не найдена.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "5":
            try:
                rid = int(input("Введите ID для удаления: "))
                confirm = input(f"Удалить запись {rid}? (да/нет): ").strip().lower()
                if confirm == "да":
                    if logic.delete_record(records, rid):
                        print("Запись удалена.")
                    else:
                        print("Запись с таким ID не найдена.")
                else:
                    print("Удаление отменено.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "6":
            stats = logic.statistics(records)
            print("\n--- Статистика ---")
            print(f"Всего записей: {stats['total']}")
            print(f"Выполнено: {stats['completed']}")
            print(f"Не выполнено: {stats['not_completed']}")
            print(f"Общее количество снимков: {stats['total_amount']}")
            print("По категориям:")
            for cat, amount in stats['by_category'].items():
                print(f"  {cat}: {amount}")

        elif choice == "7":
            try:
                storage.save_records(data_file, records)
                print("Данные успешно сохранены.")
            except OSError as e:
                print(f"Ошибка сохранения: {e}")

        elif choice == "8":
            answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
            if answer == "да":
                try:
                    storage.save_records(data_file, records)
                    print("Данные сохранены. Выход.")
                    break
                except OSError:
                    print("Ошибка сохранения.")
            elif answer == "нет":
                print("Выход без сохранения.")
                break
            else:
                print("Пожалуйста, ответьте 'да' или 'нет'.")
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
