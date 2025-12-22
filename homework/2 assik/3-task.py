s = input()

a = s[0]
op = s[1]     
b = s[2]      
c = s[4]      


if a != 'x':
    a = int(a)
if b != 'x':
    b = int(b)
c = int(c)

if a == 'x':
    if op == '+':
        x = c - b
    else:  
        x = c + b

else:
    if op == '+':
        x = c - a
    else:  
        x = a - c

print(x)
