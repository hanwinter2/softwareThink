numbers = []

for i in range(10):
    numbers.append(int(input()))

l = set()

for i in numbers:
    l.add(i%42)

print(len(l))