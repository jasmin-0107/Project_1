def Add(a,b):
    return a + b
def Sub(a,b):
    return a - b
def Mul(a,b):
    return a * b
def Div(a,b):
    if b == 0:
       return "Error: Division by zero"""
    return a / b

def main():
    print("Hello, Python!")
    a=input("input a: ")
    b=input("input b: ")
    a = int(a)
    b = int(b)
    print("a=", a, "b=", b)
    print("Calculating a+b:", Add(a, b))
    print("Calculating a-b:", Sub(a, b))
    print("Calculating a*b:", Mul(a, b))
    print("Calculating a/b:", Div(a, b))

if __name__ == "__main__":
    main()