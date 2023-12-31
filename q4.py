import sys
v, h = list(map(int, sys.stdin.readline().split()))
vertical_slash_number = int(sys.stdin.readline())
vertical_slash_list = list(map(int, sys.stdin.readline().split()))
horizontal_slash_number = int(sys.stdin.readline())
horizontal_slash_list = list(map(int, sys.stdin.readline().split()))

sequence_diff_vertical = []
sequence_diff_horizontal = []
vertical_slash_list.insert(0, 0)
vertical_slash_list.insert(len(vertical_slash_list), v)
horizontal_slash_list.insert(0, 0)
horizontal_slash_list.insert(len(horizontal_slash_list), h)

for i in range(vertical_slash_number + 1):
    sequence_diff_vertical.append(vertical_slash_list[i+1]-vertical_slash_list[i])

for i in range(horizontal_slash_number + 1):
    sequence_diff_horizontal.append(horizontal_slash_list[i+1] - horizontal_slash_list[i])


print(max(sequence_diff_vertical) * max(sequence_diff_horizontal))
