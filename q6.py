import sys
dic = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S", 29: "T", 30: "U", 31:"V", 32:"W", 33: "X", 33: 'Y', 35:"Z"}
n = int(sys.stdin.readline())
digits = [0] * 20
i = 2
while i <= n:
    digits[i-2] = n % i
    n = n // i
    digits[i-1] = n
    i += 1
digits.reverse()

j = 0
while digits[j] == 0:
    j += 1
digits = digits[j:]

digits = list(map(lambda x: dic[x], digits))
answer = ""
for i in digits:
    answer += i
print(answer)

