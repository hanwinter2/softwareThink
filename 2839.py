n = int(input())
min = 0

for i in range (n//5 + 1):
    for j in range (n//3 + 1):
        if i * 5 + j * 3 == n:
            if min == 0:
                min = i + j
            elif min > i + j:
                min = i + j

if min == 0:
    min = -1

print(min)