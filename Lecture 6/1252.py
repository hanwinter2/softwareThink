a, b = input().split()

intA = int(a, 2)
intB = int(b, 2)

c = intA + intB

c = bin(c)[2:]
print(c)