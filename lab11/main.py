import json
from pathlib import Path
from typing import Any


def validate_todos(data: Any) -> None:
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")
    seen_ids = set()
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент #{i} должен быть объектом")
        for key in ("id", "userId", "title", "completed"):
            if key not in item:
                raise ValueError(f"В элементе #{i} нет ключа {key!r}")
        if type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"id элемента #{i} должен быть положительным целым")
        if item["id"] in seen_ids:
            raise ValueError(f"Повторяющийся id: {item['id']}")
        seen_ids.add(item["id"])
        if type(item["userId"]) is not int or item["userId"] <= 0:
            raise ValueError(f"userId элемента #{i} должен быть положительным целым")
        if not isinstance(item["title"], str) or not item["title"].strip():
            raise ValueError(f"title элемента #{i} должен быть непустой строкой")
        if type(item["completed"]) is not bool:
            raise ValueError(f"completed элемента #{i} должен быть true/false")


def select_tasks(todos: list[dict], user_id: int, parameter: str) -> list[dict]:
    substring = parameter.strip().lower()
    if not substring:
        raise ValueError("Подстрока не может быть пустой")
    return [
        t for t in todos
        if t["userId"] == user_id
        and t["completed"] is True
        and substring in t["title"].lower()
    ]


def ask_user_id() -> int:
    while True:
        raw = input("Введите user_id (положительное целое): ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Ошибка: нужно положительное целое. Попробуйте снова.")


def ask_parameter() -> str:
    while True:
        raw = input("Введите подстроку для поиска в названии: ").strip()
        if raw:
            return raw
        print("Ошибка: подстрока не может быть пустой. Попробуйте снова.")


def main() -> None:
    base = Path(__file__).resolve().parent
    # Теперь читаем локальный файл, который лежит в папке
    input_path = base / "todos.json" 
    output_path = base / "selected.json"

    print("Читаем локальный файл todos.json...")
    try:
        with open(input_path, encoding="utf-8") as f:
            todos = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден в папке с программой!")
        return
    except json.JSONDecodeError as e:
        print(f"Ошибка формата JSON в файле: {e}")
        return

    print("Данные успешно загружены. Проверяем...")
    try:
        validate_todos(todos)
    except ValueError as e:
        print(f"Ошибка данных: {e}")
        return

    user_id = ask_user_id()
    parameter = ask_parameter()
    
    selected = select_tasks(todos, user_id, parameter)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(selected, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Не удалось записать {output_path}: {e}")
        return

    print(f"\nУспех! Найдено задач: {len(selected)}")
    print(f"Результат сохранён в файл: {output_path}")
    print("ID найденных задач:", [t["id"] for t in selected])


if __name__ == "__main__":
    main()
