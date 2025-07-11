def pow(n, p):
    if p == 0:
        return 1
    if p < 0:
        return pow(1/n, -p)
    return pow(n, p-1) * n

def handle_input(name, convert):
    try:
        return convert(input(f"Enter {name}: "))
    except ValueError:
        print(f"Invalid {name} input.")
        exit(1)

def main():
    n = handle_input("number", float)
    p = handle_input("exponent", int)
    result = pow(n, p)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
