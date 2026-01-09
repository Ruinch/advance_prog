s = input()

has_alnum = False
has_alpha = False
has_digit = False
has_lower = False
has_upper = False

i = 0
while i < len(s):
    ch = s[i]

    if ch.isalnum():
        has_alnum = True

    if ch.isalpha():
        has_alpha = True

    if ch.isdigit():
        has_digit = True

    if ch.islower():
        has_lower = True

    if ch.isupper():
        has_upper = True

    i = i + 1

print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)