s = input().split()

a = int(s[0])
b = int(s[1])
c = int(s[2])

print(max(a, b, c) - min(a, b, c))