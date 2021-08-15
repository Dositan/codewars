
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


assert sum_two_smallest_numbers([19, 5, 42, 2, 77]) == 7
