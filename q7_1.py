import sys
def visible(trees):
    x = 1
    maxInd = 0
    for i in range(len(trees)):
        if trees[i] > trees[maxInd]:
            maxInd = i
            x += 1
    return x

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
max1 = max2 = 0
maxScore = 0
maxIndices = [0]
for i in range(n):
    if trees[i] > trees[maxIndices[-1]]:
        maxIndices.append(i)
maxVisibleIncrease = 0
maxVisibleIndex = 0
if len(maxIndices) >= 3:
    for i in range(len(maxIndices) - 2):
        max1 = maxIndices[i]
        max2 = maxIndices[i+1]
        max3 = maxIndices[i+2]
        j = max2+1
        while trees[j] <= trees[max1]:
            j += 1

        print(max1, max2, j, max3)
        if visible(trees[j:max3]) > maxVisibleIncrease:
            maxVisibleIncrease = visible(trees[j:max3])
            maxVisibleIndex = max2

print(maxVisibleIndex)
