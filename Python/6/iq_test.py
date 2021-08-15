
def iq_test(numbers):
    numbers = [int(x) for x in numbers.split()]
    odd, even = [], []
    for n in numbers:
        even.append(n) if n % 2 == 0 else odd.append(n)
    
    return numbers.index(odd[0] if len(even) > 1 else even[0]) + 1


assert iq_test("2 4 7 8 10") == 3
