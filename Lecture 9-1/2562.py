value = int(input())
n = 0

for i in range(8):
	tem = int(input())
	if tem > value:
		value = tem
		n = i + 1

print(value)
print(n+1)