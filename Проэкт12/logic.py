def validate_records(records: list[dict]) -> None:
    """Проверяет корректность всех записей."""
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            raise ValueError(f"Запись #{i} должна быть словарем")
        for key in ("id", "title", "category", "amount", "completed"):
            if key not in rec:
                raise ValueError(f"В записи #{i} нет ключа {key}")

        if type(rec["id"]) is not int or rec["id"] <= 0:
            raise ValueError(f"id записи #{i} должен быть положительным целым")
        if rec["id"] in seen_ids:
            raise ValueError(f"Повторяющийся id: {rec['id']}")
        seen_ids.add(rec["id"])

        if not isinstance(rec["title"], str) or not rec["title"].strip():
            raise ValueError(f"title записи #{i} должен быть непустой строкой")
        if not isinstance(rec["category"], str) or not rec["category"].strip():
            raise ValueError(f"category записи #{i} должна быть непустой строкой")

        # Проверка для 15 варианта: amount - целое число >= 0
        if type(rec["amount"]) is not int or rec["amount"] < 0:
            raise ValueError(f"amount записи #{i} должен быть целым >= 0")

        if type(rec["completed"]) is not bool:
            raise ValueError(f"completed записи #{i} должен быть true/false")

def add_record(records: list[dict], title: str, category: str, amount: int) -> dict:
    new_id = max((r["id"] for r in records), default=0) + 1
    new_rec = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False
    }
    records.append(new_rec)
    return new_rec

def find_records(records: list[dict], query: str) -> list[dict]:
    if not query.strip():
        raise ValueError("Поисковый запрос не может быть пустым")
    q = query.strip().lower()
    return [r for r in records if q in r["title"].lower()]

def set_completed(records: list[dict], record_id: int, completed: bool) -> bool:
    for r in records:
        if r["id"] == record_id:
            r["completed"] = completed
            return True
    return False

def delete_record(records: list[dict], record_id: int) -> bool:
    for i, r in enumerate(records):
        if r["id"] == record_id:
            del records[i]
            return True
    return False

def statistics(records: list[dict]) -> dict:
    total = len(records)
    completed = sum(1 for r in records if r["completed"])
    total_amount = sum(r["amount"] for r in records)

    by_category = {}
    for r in records:
        cat = r["category"]
        by_category[cat] = by_category.get(cat, 0) + r["amount"]

    sorted_categories = {k: by_category[k] for k in sorted(by_category)}

    return {
        "total": total,
        "completed": completed,
        "not_completed": total - completed,
        "total_amount": total_amount,
        "by_category": sorted_categories
    }
