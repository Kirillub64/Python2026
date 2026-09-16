# Обмен значениями через третью переменную
first_room = "227"
second_room = "401"

print(f"До обмена: first_room = {first_room}, second_room = {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print(f"После обмена: first_room = {first_room}, second_room = {second_room}")
