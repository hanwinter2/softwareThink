n = int(input())
for i in range(n):
	ch = input()
	se = 0
	point = 0

	for s in ch:
		if s == "O":
			se += 1
			point += se
		else:
			se = 0

	print(point)