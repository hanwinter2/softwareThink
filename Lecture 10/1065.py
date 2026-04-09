def ifHansu(n):
	if n < 100:
		return True
	else:
		st = str(n)
		gap = int(st[0]) - int(st[1])
		for i in range(len(str(n))-1):
			if gap != int(st[i]) - int(st[i+1]):
				return False
		return True

a = int(input())
hansuNum = 0
for i in range(1, a+1):
	if ifHansu(i):
		hansuNum += 1

print(hansuNum)