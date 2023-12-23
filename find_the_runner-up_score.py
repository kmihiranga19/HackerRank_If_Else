if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    numbers = list(arr)

    max_number = max(numbers)

    second_max_number = max(num for num in numbers if num < max_number)

    print(second_max_number)
