s = input()
words = s.split()
count = 0

for w in words:
    if w.lower().startswith("e"):
        count += 1

print(count)