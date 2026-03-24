a, b = input().split()

a = int(a)
b = int(b)
str = ''

if a>b:
    str = ">"
if a<b:
    str = "<"
if a==b:
    str = "=="
    
print(str)