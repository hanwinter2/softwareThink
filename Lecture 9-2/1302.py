n = int(input())

seller = []

for i in range(n):
	seller.append(input())

seller.sort()
sellerSet = set(seller)
sellerDic = {}
for i in list(sellerSet):
	a = 0
	for j in seller:
		if i == j:
			a += 1
	sellerDic.update({i:a})

max = seller[0]
maxIndex = sellerDic.get(seller[0])

for i in list(sellerSet):
	if sellerDic.get(i) > maxIndex:
		max = i
		maxIndex = sellerDic.get(i)
	elif sellerDic.get(i) == maxIndex:
		if i < max:
			max = i

print(max)