
import random

#1

l1 = []
for i in range(10):
    l1.append(random.randint(0, 10))
y = list(l1)
print(y, end=" ")

print("\n")


t1 = tuple(y)
print(t1)
#2
l2 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

x, y, t = tuple(l2)

a = list(x)
s = list(y)
d = list(t)

a[2] = 100
s[2] = 100
d[2] = 100

l3 = tuple()

l3 = a, s, d

print(l3)

#4

s1 = set()
s2 = []
for e in range(10):
    s2.append(random.randint(1, 10))


s1 = set(s2)
print(s1)

A = int(input("Enter value: "))
if A in s1:
    print("yes")
else:
	print("no")

#5
s3 = set()
s4 = set()
li = []
li2 = []
for s3t in range(10):
    li.append(random.randint(0, 10))

for s4t in range(10):
    li2.append(random.randint(0, 10))


s3 = set(li)
s4 = set(li2)

print(s3)
print(s4)
s5 = s3 & s4
if s3 & s4:
    print("yes: {}".format(s5))
else:
    print("no")
#6
A1 = set()
B = set()

li1 = []
li3 = []
for s5t in range(10):
    li1.append(random.randint(0, 10))

for s6t in range(10):
    li3.append(random.randint(0, 10))

A1 = set(li1)
B = set(li3)
print(A1)
print(B)

s6 = A1.difference(B)
print(s6)








