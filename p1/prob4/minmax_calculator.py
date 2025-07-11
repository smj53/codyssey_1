
def getArrayInput():
    arr = input("Enter a list of numbers separated by spaces: ").split()
    number_list = list(map(float, arr))
    if len(number_list) == 0:
        raise ValueError()
    return number_list

def getMin(arr):
    min_value = float('inf')
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

def getMax(arr):
    max_value = float('-inf')
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

def main():
    try:
        arr = getArrayInput()
        print(f"Min: {getMin(arr)}, Max: {getMax(arr)}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    except KeyboardInterrupt:
        return
    except EOFError:
        return

if __name__ == "__main__":
    main()