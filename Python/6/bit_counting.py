
def count_bits(n):
    return format(n, 'b').count('1')


assert count_bits(1234) == 5
assert count_bits(234123) == 9
