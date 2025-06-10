def Add(a,b):
    return a + b
def Sub(a,b):
    return a - b

def main():
    print("Hello, Python!")
    a=5
    b=3
    print("a=", a, "b=", b)
    print("Calculating a+b:", Add(a, b))
    print("Calculating a-b:", Sub(a, b))
    print("Calculating a+b, a-b:", Add(a, b), Sub(a, b))

if __name__ == "__main__":
    main()