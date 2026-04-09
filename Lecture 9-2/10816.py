from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
numbers2 = list(map(int, input().split()))

count = Counter(numbers)

result = [str(count[q]) for q in numbers2]
print(" ".join(result))