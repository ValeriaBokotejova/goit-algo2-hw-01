import random
import colorama

from colorama import Fore

colorama.init(autoreset=True)

def quick_select(arr, k):
    """
    Returns the k-th smallest element in the array (1-based index).
    Uses pivot selection and partitioning without fully sorting.
    Average time complexity: O(n).
    """
    if arr is None or k < 1 or k > len(arr):
        raise ValueError("Invalid k or empty array")

    pivot = random.choice(arr)

    lows = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]

    if k <= len(lows):
        return quick_select(lows, k)
    elif k > len(lows) + len(pivots):
        return quick_select(highs, k - len(lows) - len(pivots))
    else:
        return pivot


if __name__ == "__main__":

    numbers = [20, 15, 7, 4, 92, 34, 14, 2, 3]
    print(Fore.YELLOW + "Array of numbers: " + str(numbers))

    k = 3
    result = quick_select(numbers, k)
    print(Fore.CYAN + f"{k}rd smallest element: {result}")
