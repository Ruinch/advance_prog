s = input()

max_count = 0
cur = 0

for ch in s:
    if ch == "n":
        cur += 1
        max_count = max(max_count, cur)
    else:
        cur = 0

s = s.replace("!", ".")

print("Longest n seq:", max_count)
print(s)
