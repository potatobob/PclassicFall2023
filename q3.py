import sys
coins = int(sys.stdin.readline())
times_spells = sys.stdin.readline()
times_values = list(map(int, sys.stdin.readline().split()))
add_spells = sys.stdin.readline()
add_values = list(map(int, sys.stdin.readline().split()))
for spells in add_values:
    coins += spells
for spells in times_values:
    coins *= spells
print(coins)
