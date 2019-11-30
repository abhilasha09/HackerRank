#!/bin/python3

import sys


def max_mul(s, n, k):
    a = []
    for i in range(n-k+1):
        a.append(s[i:k+i])
    max = -1
    mul = 1
    for j in a:
        for p in j:
            mul *= int(p)
        if mul > max:
            max = mul
        mul = 1
    return max

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    s = input().strip()
    print(max_mul(s, n, k))
