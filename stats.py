import math
import os
import sys

__INVALID_INPUT = "invalid input (-_-)\n" \
                  "exit program..."


def exit_program():
    print(__INVALID_INPUT)
    sys.exit(1)


def get_numbers():
    arguments_length = len(sys.argv)

    if arguments_length == 1:
        return get_numbers_from_stream(sys.stdin)
    elif arguments_length == 2:
        return get_file_numbers(sys.argv[1])
    else:
        exit_program()

def clean_numbers(numbers):
    return numbers.strip("\n").replace(",", ".").split(" ")


def convert_to_floats(numbers):  # str or list as parameters
    if isinstance(numbers, str):
        numbers = clean_numbers(numbers)
    else:
        tmp_numbers = []
        for number in numbers:
            numbers = clean_numbers(number)
            tmp_numbers.extend(numbers)
        numbers = tmp_numbers

    numbers = list(filter(None, numbers))

    try:
        return list(map(float, numbers))
    except ValueError:
        exit_program()


def get_numbers_from_stream(file):
    numbers = file.readlines()
    return convert_to_floats(numbers)

def get_file_numbers(file_name: str):
    if os.path.isfile(file_name):
        with open(file_name) as file:
            return get_numbers_from_stream(file)
    else:
        exit_program()


def calculate_mean(numbers: list):
    return sum(numbers) / len(numbers)


def calculate_median(numbers: list):
    numbers.sort()
    numbers_length = len(numbers)

    index = int(numbers_length / 2)
    if numbers_length % 2 == 0:
        return (numbers[index] + numbers[index - 1]) / 2

    return numbers[index]


def calculate_standard_deviation(numbers: list):
    if len(numbers) < 2:
        return "At least 2 numbers needed (-_-)"

    return math.sqrt(calculate_variance(numbers))


# found in
# https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/#
# implemented in a similar way
def calculate_variance(numbers: list):
    mean = calculate_mean(numbers)
    deviations = [(number - mean) ** 2 for number in numbers]

    return sum(deviations) / (len(numbers) - 1)  # variance


def print_result():
    numbers = get_numbers()

    print("mean: " + str(calculate_mean(numbers)))
    print("median: " + str(calculate_median(numbers)))
    print("standard deviation: " + str(calculate_standard_deviation(numbers)))


if __name__ == "__main__":
    print_result()
