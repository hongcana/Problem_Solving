import sys
read = sys.stdin.readline
A, B, C = list(map(int, read().split()))


def div(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return (div(a, b//2, c) ** 2) % c
    else:
        return ((div(a, b//2, c)**2)*a) % c


print(div(A, B, C))
