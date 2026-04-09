import sys

input = sys.stdin.readline

limit, students = map(int, input().split())

studentsDic = {}
for i in range(students):
    studentId = input().strip()
    studentsDic[studentId] = i

orderList = []
for studentId, order in studentsDic.items():
    orderList.append((order, studentId))

orderList.sort()

count = 0
for order, studentId in orderList:
    if count == limit:
        break
    print(studentId)
    count += 1