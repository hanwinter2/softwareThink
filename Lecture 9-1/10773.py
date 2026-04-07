numbers = []

for i in range(int(input())):
	n = int(input())
	if n == 0:
		del numbers[len(numbers)-1]
	else:
		numbers.append(n)

sum = 0
for i in numbers:
	sum += i

print(sum)