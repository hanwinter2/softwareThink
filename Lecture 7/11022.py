r = int(input())

for i in range(r):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print("Case #" + str(i+1) + ": " + str(a) + " + " + str(b) + " = " + str(a+b))