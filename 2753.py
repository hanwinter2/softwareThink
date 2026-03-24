year = int(input())
bool = 0

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            bool = 1
    else:
        bool = 1

print(bool)