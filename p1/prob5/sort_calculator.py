
def getArrayInput():
    arr = input("Enter a list of numbers separated by spaces: ").split()
    number_list = list(map(float, arr))
    if len(number_list) == 0:
        raise ValueError()
    return number_list

def getSorted(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def main():
    try:
        arr = getArrayInput()
        print(f"Sorted: {' '.join(map(str, getSorted(arr)))}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    except KeyboardInterrupt:
        return
    except EOFError:
        return
    
if __name__ == "__main__":
    main()