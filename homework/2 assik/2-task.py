a = input()
b = input()

m = len(b)
count = 0

shifts = []
i = 0
while i < m:
    shift = b[i:] + b[:i]
    shifts.append(shift)
    i += 1

i = 0
while i <= len(a) - m:
    part = a[i:i+m]
    if part in shifts:
        count += 1
    i += 1

print(count)
