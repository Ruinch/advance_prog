n, m = map(int, input().split())
s = input()

words = []
i = 0

while i <= n - m:
    part = s[i:i+m]
    if part not in words:
        words.append(part)
    i += 1

print(len(words))
