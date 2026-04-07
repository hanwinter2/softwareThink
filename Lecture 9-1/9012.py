for n in range(int(input())):
	boolean = ''
	ch = list(input())

	while True:
		changed = False
		for i in range(1, len(ch)):
			if ch[i-1] == "(":
				if ch[i] == ")":
					del ch[i-1]
					del ch[i-1]
					changed = True
					break
		
		if len(ch) == 0:
			break

		if changed == False:
			boolean = "NO"
			break
	
	if boolean == '':
		boolean = "YES"
	print(boolean)