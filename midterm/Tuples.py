#for python 3
# n = int(input())

# nums = list(map(int, input().split()))

# i = 0
# t = []

# while i < n:
#     t.append(nums[i])
#     i = i + 1

# t = tuple(t)

# print(hash(t))

#for python 2 
n = int(input())
t = tuple(map(int, input().split()))

print(hash(t))
