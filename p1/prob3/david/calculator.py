def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise Exception("Error: Division by zero.")
    return a / b

ops = {"+": add, "-": subtract, "*": multiply, "/": divide}

def validateInput(a, b, op):
    try:
        numA = float(a)
        numB = float(b)
    except:
        raise Exception("Invalid Input: Not a float")
    if op not in ops.keys():
        raise Exception("Invalid operator.")
    return (numA, numB, op)

def getInput():
    arr = input("input a b: ").split()
    if len(arr) != 2:
        raise Exception("Invalid Input: format should be 'a b'")
    op = input("input operator: ")
    return validateInput(arr[0], arr[1], op)

def getBonusInput():
    arr = input("input a <operator> b: ").split()
    if len(arr) != 3:
        raise Exception("Invalid Input: format should be 'a operator b'")
    return validateInput(arr[0], arr[2], arr[1])
    
def selectType(ans):
    if ans == "1":
        a, b, op = getInput()
    elif ans == "2":
        a, b, op = getBonusInput()
    elif ans == "3":
        exit(0)
    else:
        print("Wrong input")
        return
    print(f"Result: <{ops[op](a, b)}>")

if __name__ == "__main__":
    while True:
        try:
            ans = input("select type of input (1 - default, 2 - bonus, 3 - exit): ")
            selectType(ans)
        except EOFError:
            exit(0)
        except KeyboardInterrupt:
            exit(0)
        except Exception as e:
            print(e)
        
