import json
from pathlib import Path

def load_records(path: Path) -> list[dict]:
    """Читает JSON. Если файла нет — возвращает пустой список."""
    if not path.exists():
        print("Файл data.json не найден. Начинаем с пустого списка.")
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Ошибка чтения файла: {e}")
        raise

def save_records(path: Path, records: list[dict]) -> None:
    """Сохраняет список записей в JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
