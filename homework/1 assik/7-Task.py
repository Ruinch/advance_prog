a = float(input("First number: ")) 
op = input("Operation (+, -, *, /): ") 
b = float(input("Second number: ")) 

if op == "+": 
    print(a + b) 
elif op == "-": 
    print(a - b) 
elif op == "*": 
    print(a * b) 
elif op == "/": 
    result = a / b if b != 0 else "Error" 
else: 
    print("Unknown operation") 
