text = input("Введите текст: ")

count = text.count(":")
new_text = text.replace(":", "-")

print("Замен:", count)
print(new_text)
