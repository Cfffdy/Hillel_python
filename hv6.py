
#1

def calculations(a, b):
    z = a + b
    x = a - b
    return z, x

a = int(input("Enter value: "))
b = int(input("Enter value: "))
temp = calculations(a, b)
sum, sub = calculations(a, b)
print(temp)
print(sum)
print(sub)

#2
import random

l = []

for i in range(10):
    l.append(random.randint(0, 10))
print(l)

def sum(*args):
    total = 0
    for c in l:
        total += c
    return total


print(sum(l))

#4
v = str(input("Enter name: "))
m = str(input("Enter salary: "))

def showEmployee():
    n = dict()
    n[0] = (v + " " + m)
    print(n[0])
    h = int(b)
    if h != 0:
        p = str(9000)
        n[1] = (v + " " + p)
        print(n[1])
    return n[0]

showEmployee()