import sys
x = sys.stdin.readline()
for item in range(int(x)):
    item = sys.stdin.readline()
    print(int(item)+1)
    item = sys.stdin.readline()
    print(str(item)[:-1] + "a")
    item = sys.stdin.readline()
    sum = 0
    for items in item.split():
        sum+= int(items)
    print(sum)
