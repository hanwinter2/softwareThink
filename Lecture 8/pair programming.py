a = int(input())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
print("         " + str(a) + "월")
print("일 월 화 수 목 금 토")

b = 5

for i in range(0, a):
    b = b+days[i]

firstDay = b%7
if firstDay == 0:
    firstDay = 7
string = "   " * (firstDay-1)

for i in range(1, days[a]+1):
    if i < 10:
            string = string + " " + str(i) + " "
    else:
        string = string + str(i) + " "
    if (firstDay - 1 + i)%7 == 0:
        print(string)
        string = ""
    if i == days[a]:
        if string != "":
            print(string)