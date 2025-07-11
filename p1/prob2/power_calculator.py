def power(n, p):
    if p < 0:
        return power(1/n, -p)
    num = 1
    while p > 0:
        num = num * n
        p = p - 1
    return num

def handle_input(name, convert):
    try:
        return convert(input(f"Enter {name}: "))
    except ValueError:
        print(f"Invalid {name} input.")
        exit(1)

def main():
    n = handle_input("number", float)
    p = handle_input("exponent", int)
    result = power(n, p)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
