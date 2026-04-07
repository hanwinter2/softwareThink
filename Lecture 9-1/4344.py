a = int(input())

for i in range(a):
    numbers = list(map(int, input().split()))
    sum = 0
    student = 0
    for score in range(1, len(numbers)):
        sum = sum+numbers[score]
    for score in range(1, len(numbers)):
        if sum/numbers[0] < numbers[score]:
            student += 1
    
    print("{:.3f}%".format(student/numbers[0]*100))