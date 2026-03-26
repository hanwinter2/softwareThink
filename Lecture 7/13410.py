a, b = input().split()

a = int(a)
b = int(b)
c = 0
max_val = 0

for i in range(1, b+1):
    c = int(str(i * a)[::-1])
    
    if c > max_val:
        max_val = c

print(max_val)