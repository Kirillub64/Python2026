VOWELS = "аеёиоуыэюя"

text = input("Введите текст: ")
words = text.split()

count = 0

for word in words:
    clean = word.strip(".,!?;:").lower()
    if clean == "":
        continue
    if clean[0] in VOWELS:
        print(clean)
        count += 1

if count == 0:
    print("Нет совпадений")

print("Количество:", count)
