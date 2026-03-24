hour, minute, second = input().split()

hour = int(hour)
minute = int(minute)
second = int(second)

second = second + int(input())

while minute > 59 or second > 59 or hour > 23:
    if minute > 59:
        minute = minute - 60
        hour = hour + 1
    if second > 59:
        second = second - 60
        minute = minute + 1
    if hour > 23:
        hour = hour - 24

print(str(hour) + " " + str(minute) + " " + str(second))