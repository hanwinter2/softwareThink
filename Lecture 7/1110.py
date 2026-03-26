a = int(input())
cycles = 0
current = a
next = 0

while True:
    if current < 10:
        next = current
    else:
        next = current%10 + current//10
    
    current = current%10*10 + next%10
    cycles += 1
    if current == a:
        break

print(cycles)
