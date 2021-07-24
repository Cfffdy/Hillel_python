# 1
l1 = [1, 2, 1, 3, 1]
l2 = []
for i in range(1, 4):
    print(i, end=" ")
for x in l1[-1:4]:
    print(l2, end="")

# 2
a = int(input("Введите количество копий списка:"))
l3 = [1, 2, 5, "abc", 9]
for i in range(a):
    print(l3)
# 4
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dict()
dic4[1] = dic1, dic2, dic3
print(dic4[1])
# 5
d1 = dict()
for c in range(1, 16):
    print(c, end=" ")
print()
for v in range(1, 16):
    v **= 2
    print(v, end=" ")



