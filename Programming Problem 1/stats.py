def mean(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_frequency = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_frequency]

    if len(modes) == 1:
        return modes[0]
    else:
        raise ValueError("The list has no unique mode.")
