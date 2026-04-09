import sys

input = sys.stdin.read().split()

n = int(input[0])
m = int(input[1])

hear = set(input[2 : 2 + n])

see = set(input[2 + n : 2 + n + m])

result = sorted(list(hear & see))

print(len(result))
for name in result:
    print(name)