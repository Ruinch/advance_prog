n = int(input())
arr = list(map(int, input().split()))


i = 0
max_val = arr[0]

while i < n:
    if arr[i] > max_val:
        max_val = arr[i]
    i = i + 1


i = 0
runner = None

while i < n:
    if arr[i] != max_val:
        if runner is None or arr[i] > runner:
            runner = arr[i]
    i = i + 1

print(runner)
