# variant.py — вариант 15: Туристический магазин
order_name = "Поход"
customer = "Туристический магазин"

name1 = "Фонарики"
qty1 = 3
price1 = 12.50

name2 = "Компасы"
qty2 = 2
price2 = 20.00

delivery = 10.00
paid = 100.00

sum1 = qty1 * price1
sum2 = qty2 * price2
goods_total = sum1 + sum2
total = goods_total + delivery
total_qty = qty1 + qty2
change = paid - total

print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer}")
print(f"{name1} | {qty1} | {price1:.2f} | {sum1:.2f}")
print(f"{name2} | {qty2} | {price2:.2f} | {sum2:.2f}")
print(f"Стоимость товаров: {goods_total:.2f}")
print(f"Доставка: {delivery:.2f}")
print(f"Итого: {total:.2f}")
print(f"Всего единиц: {total_qty}")
print(f"Сдача: {change:.2f}")
