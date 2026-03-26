ch = input()

sum = 0

for c in ch:
    if 'a' <= c <= 'z':
        sum = sum + ord(c) - ord('a') + 1
    if 'A' <= c <= 'Z':
        sum = sum + ord(c) - ord('A') + 27

prime = True

for i in range(2, sum):
    if sum%i == 0:
        prime = False

if prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")