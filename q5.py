import sys
n, k = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
prefSum, maxPref, maxInd, maxScore = 0,0,0,0
for i in range(min(n, k)):
    if i+1 != n:
        prefSum += A[i+1]
        if A[i+1] > A[maxInd] or i == 0:
            maxInd = i + 1
            maxPref = prefSum
    maxScore = max(maxScore, maxPref + A[maxInd] * (k-maxInd))
maxScore = max(maxScore, A[0] * k)
print(maxScore)
