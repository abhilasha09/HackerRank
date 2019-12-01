#!/bin/python3

import sys

m=-1;
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m=-1;
    for a in range(3,n//3+1):
        b=(a*a-(a-n)*(a-n))//(2*(a-n))
        c=n-a-b
        if c*c==a*a+b*b:
            if a*b*c>m:
                m=a*b*c
    print(m)

