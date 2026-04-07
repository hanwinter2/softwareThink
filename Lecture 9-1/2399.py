n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

total = 0

for i in range(n-1):
    d = numbers[i+1] - numbers[i]
    total += d * (i+1) * (n-i-1)

print(2 * total)