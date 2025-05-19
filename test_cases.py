from bubble_sort_basic import bubble_sort
from bubble_sort_optimized import bubble_sort_optimized

def run_tests():
    test_cases = [
        ("Random array", [5, 3, 8, 4, 2]),
        ("Already sorted", [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1]),
        ("All identical", [7, 7, 7, 7, 7]),
        ("Empty array", []),
        ("Single element", [42])
    ]

    for name, case in test_cases:
        basic_sorted = bubble_sort(case.copy())
        optimized_sorted = bubble_sort_optimized(case.copy())
        print(f"\n{name}:\nOriginal: {case}\nBasic: {basic_sorted}\nOptimized: {optimized_sorted}")

if __name__ == "__main__":
    run_tests()
