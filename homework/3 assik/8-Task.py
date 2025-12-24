#first part

# n = int(input())
# i = 1
# while i <= n:
#     temp = i
#     ok = True

#     while temp > 0:
#         digit = temp % 10

#         if digit == 0 or i % digit != 0:
#             ok = False
#             break

#         temp = temp // 10

#     if ok:
#         print(i, end=" ")
#     i = i + 1



#second part

def swap_first_last(arr):
    temp = arr[0]
    arr[0] = arr[len(arr) - 1]
    arr[len(arr) - 1] = temp



# m = int(input())

# arr = []
# i = 0
# while i < m:
#     arr.append(int(input()))
#     i = i + 1

# i = 0
# while i < m:
#     print(arr[i], end=" ")
#     i = i + 1

# print()

# swap_first_last(arr)

# i = 0
# while i < m:
#     print(arr[i], end=" ")
#     i = i + 1
