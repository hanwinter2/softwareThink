n = int(input())
numbers = list(map(int, input().split()))
numbers.sort

sum = 0

for i in range(n-1):
    d = numbers[i+1] - numbers[i]
    sum += d * (i+1) * (n-i-1)

print(2 * sum)