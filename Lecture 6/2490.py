d = 0

while True:
    yut = list(map(int, input().split()))
    yutNumber = 0

    for i in range(len(yut)):
        if yut[i] == 0:
            yutNumber = yutNumber + 1
            

    yutStr = ["E", "A", "B", "C", "D"]
    print(yutStr[yutNumber])
    d = d+1
    
    if d==3:
        break
    