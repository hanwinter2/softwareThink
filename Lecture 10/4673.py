def d(n):
	str_n = str(n)
	total = 0
	for i in str_n:
		total += int(i)
	total += n
	return total

numSet = set(range(1, 10000))

for i in range(1, 10000):
	numSet.discard(d(i))

for i in list(numSet):
	print(i)