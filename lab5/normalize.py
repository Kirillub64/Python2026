text = input("Введите текст: ")

stripped = text.strip()
words = stripped.split()
normalized = " ".join(words)

print("Исходная длина:", len(text))
print("Новая длина:", len(normalized))
print("Нормализованный текст:", normalized)
print("Слов:", len(words))
