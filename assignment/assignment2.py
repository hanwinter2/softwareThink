import random

n = int(input())

def create_random_list(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randrange(1, n**2 * 10))
        matrix.append(row)
    return matrix

def print_list(matrix):
    for i in matrix:
        string = ''
        for j in i:
            string += str(j) + " "
        print(string)

a = create_random_list(n)

at = []
for i in range(n):
    at2 = []
    for j in range(n):
        at2.append(0)
    at.append(at2)

for i in range(n):
    for j in range(n):
        at[i][j] = a[j][i]

print_list(a)
print_list(at)