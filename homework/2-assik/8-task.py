s1 = input()
s2 = input()


if len(s1) != len(s2):
    print("NO")
else:
    freq1 = {}
    freq2 = {}


    i = 0
    while i < len(s1):
        ch = s1[i]
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
        i += 1


    i = 0
    while i < len(s2):
        ch = s2[i]
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
        i += 1


    if freq1 == freq2:
        print("YES")
    else:
        print("NO")
