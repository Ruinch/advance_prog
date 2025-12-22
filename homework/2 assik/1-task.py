s = input()
i = 0
count = 0

while i <= len(s) - 5:
    part = s[i:i+5]
    if part == ">>-->" or part == "<--<<":
        count += 1
    i += 1

print(count)