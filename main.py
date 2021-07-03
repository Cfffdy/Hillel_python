# 1
a = int(input("Машина проезжает за день км:"))
b = int(input("Дан маршрут длиною в км:"))
c = int(b/a)
print("Вывод:нужно {} дней, чтобы проехать данный маршрут".format(c))
# 3
print("Введите любые три числа:")
ara = int(input())
aba = int(input())
aca = int(input())
if ara>aba and ara>aca:
    print("{} это максимальное число".format(ara))
elif aba>ara and aba>aca:
    print("{} это максимальное число".format(aba))
elif aca>ara and aca>aba:
    print("{} это максимальное число".format(aca))
else:
    print(":(")
# 4
print("Введите год:")
e = int(input())
if e % 4 == 0:
    print("Вы ввели высокосный год")
else:
    print("Обычный год")
# 5
gg = int(input("Введите число:"))
if gg % 2 == 0:
    print("Четное число")
else:
    print("Нечетное число")