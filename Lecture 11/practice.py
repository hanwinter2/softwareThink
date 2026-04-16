def hanoi(n, start, end, aux):
    if n == 1:
        print("n: {} | {} -> {}".format(n, start, end))
    else:
        hanoi(n-1, start, aux, end)
        print("n: {} | {} -> {}".format(n, start, end))
        hanoi(n-1, aux, end, start)

n = int(input())
hanoi(n, 1, 3, 2)