s = int(input())

string = ''

for i in range(1, s+1):
    string = ''
    for j in range(1, i):
        string = string + " "
    for j in range(1, 2*s - 2*i + 2):
        string = string + "*"
    print(string)

for i in range(1, s): # 1,5
    string = ''
    for j in range(1, s-i):
        string = string + " "
    for j in range(1, 2*i + 2):
        string = string + "*"
    print(string)
