n = int(input())

allowed = "ABCEHKMOPTXY"

for _ in range(n):
    s = input()

    ok = True

    if len(s) != 6:
        ok = False
    else:
        if s[0] not in allowed:
            ok = False
        if not (s[1].isdigit() and s[2].isdigit() and s[3].isdigit()):
            ok = False
        if s[4] not in allowed or s[5] not in allowed:
            ok = False

    if ok:
        print("Yes")
    else:
        print("No")
