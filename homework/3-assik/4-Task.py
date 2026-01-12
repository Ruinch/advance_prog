#first part

# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())

# num = A * D
# den = B * C

# a = num
# b = den

# while b != 0:
#     r = a % b
#     a = b
#     b = r

# gcd = a

# num = num // gcd
# den = den // gcd

# print(num, "/", den)


#second part

def inside_circle(x, y, a, b, r):
    dx = x - a
    dy = y - b

    if dx * dx + dy * dy <= r * r:
        return True
    else:
        return False


        
# a = float(input())
# b = float(input())
# r = float(input())


# n = 3 
# count = 0
# i = 0

# while i < n:
#     x = float(input())
#     y = float(input())

#     if inside_circle(x, y, a, b, r):
#         count = count + 1

#     i = i + 1

# print(count)
