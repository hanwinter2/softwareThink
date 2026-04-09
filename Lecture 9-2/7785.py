n = int(input())
enteredPeople = set()
for i in range(n):
	people = input().split()
	if people[1] == "enter":
		enteredPeople.add(people[0])
	else:
		enteredPeople.discard(people[0])

result = sorted(list(enteredPeople), reverse=True)
for p in result:
	print(p)