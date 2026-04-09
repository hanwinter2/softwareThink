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