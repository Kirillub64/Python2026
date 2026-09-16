total = 21
capacity = 10

full = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity

print("Полных подносов:", full)
print("Остаток порций:", remainder)
print("Всего подносов:", min_units)
