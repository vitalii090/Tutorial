num = int(input("Введіть число від 0 до 100: "))
sum = 0
i = 1

while i <= num:
    sum += i
    i += 1

print("Сума чисел від 1 до", num, "дорівнює", sum)