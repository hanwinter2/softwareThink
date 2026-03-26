n, x = input().split()

n = int(n)
x = int(x)

number = list(map(int, input().split()))

s = ''

for i in range(n):
    if number[i] < x:
        if s == '':
            s = str(number[i])
        else:
            s = s + " " + str(number[i])

print(s)