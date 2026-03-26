max = 0
people = 0

while True:
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)

        if people > 0:
            people = people - a + b
        else:
            people = people + b
    
        if people > max:
            max = people
    except:
        break

print(max)
