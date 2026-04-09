<<<<<<< HEAD
from collections import Counter

limit, students = input().split()
limit = int(limit)
students = int(students)
studentsList = []

for i in range(students):
	studentsList.append(input())

studentsDic = {}

for i in range(len(studentsList)):
	studentsDic[studentsList[i]] = i

orderList = []
for studentId, order in studentsDic.items():
    orderList.append([order, studentId])

orderList.sort()

for i in range(min(limit, len(orderList))):
    print(orderList[i][1])
=======
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
>>>>>>> 51b4b3231624a70aeafefa2d1f54553237b3aaa6
