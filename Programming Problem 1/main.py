import stats

def main():
    numbers = []
    print("Enter numbers separated by spaces:")
    try:
        numbers = list(map(float, input().strip().split()))
        if not numbers:
            raise ValueError("You must provide at least one number.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    try:
        print(f"Mean: {stats.mean(numbers)}")
        print(f"Median: {stats.median(numbers)}")
        print(f"Mode: {stats.mode(numbers)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
