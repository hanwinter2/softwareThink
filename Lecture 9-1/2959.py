numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

vertical = 0
horizontal = 0

for i in range(len(numbers)):
    if(i+1)%2 != 0:
        if horizontal == 0:
            horizontal = numbers[0]
        elif horizontal > numbers[0]:
            horizontal = numbers[0]
        del numbers[0]
        numbers.sort()
    else:
        if vertical == 0:
            vertical = numbers[0]
        elif vertical > numbers[0]:
            vertical = numbers[0]
        del numbers[0]
        numbers.sort(reverse=True)

print(vertical * horizontal)