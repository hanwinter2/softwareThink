star = int(input())

for i in range(1, 2*star+1):
    string = ''
    if i%2 != 0:
        for j in range(1, star+1):
            if j%2 != 0:
                string = string + "*"
            else:
                string = string + " "
    else:
        for j in range(1, star+1):
            if j%2 == 0:
                string = string + "*"
            else:
                string = string + " "
    print(string)