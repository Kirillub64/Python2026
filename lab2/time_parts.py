total_seconds = 4000

hours = total_seconds // 3600
left = total_seconds % 3600
minutes = left // 60
seconds = left % 60

print(hours, "ч", minutes, "мин", seconds, "с")
