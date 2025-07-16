import colorama
from colorama import Fore

colorama.init(autoreset=True)

def find_min_max(arr):
    """
    Recursively finds the minimum and maximum elements in an array.
    Returns a tuple (min, max).
    Time complexity: O(n).
    """
    n = len(arr)
    if n == 0:
        raise ValueError("Array is empty")
    if n == 1:
        return arr[0], arr[0]
    if n == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    mid = n // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return (min(left_min, right_min), max(left_max, right_max))

if __name__ == "__main__":
    numbers = [20, 15, 7, 4, 92, 34, 14, 2, 3]
    min_val, max_val = find_min_max(numbers)

    print(Fore.YELLOW + "Array of numbers:", numbers)
    print(Fore.GREEN + f"Minimum value: {min_val}")
    print(Fore.CYAN + f"Maximum value: {max_val}")
