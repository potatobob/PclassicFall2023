import sys
import math

for i in range(int(sys.stdin.readline())):
    n,k = list(map(int, sys.stdin.readline().split()))
    if math.floor(math.log(n, 10)) == math.floor(math.log(n+k, 10)):
        print("no")
    else:
        print("yes")
