import math

def isSosu(n):
	if n == 1:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n%i == 0:
			return False
	return True

minNum = int(input())
maxNum = int(input())
sosuList = []

for i in range(minNum, maxNum + 1):
	if isSosu(i):
		sosuList.append(i)

if len(sosuList) == 0:
	print("-1")
else:
	sum = 0
	for i in sosuList:
		sum += i
	print(sum)
	print(min(sosuList))