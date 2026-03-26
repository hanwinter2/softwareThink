a = int(input())
bcd = int(input())

b = int(bcd/100)
c = int(bcd/10) - b * 10
d = bcd - b*100 - c*10

print(a * d)
print(a * c)
print(a * b)
print(a * bcd)