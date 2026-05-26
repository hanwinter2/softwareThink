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
            string += f"{j:5d} " 
        print(string)

a = create_random_list(n)
b = create_random_list(n)
c = create_random_list(n)

ab = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    ab.append(row)

for i in range(n):
    for j in range(n):
        for k in range(n):
            ab[i][j] += a[i][k] * b[k][j]

abc = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    abc.append(row)

for i in range(n):
    for j in range(n):
        abc[i][j] = ab[i][j] + c[i][j]

print_list(abc)
