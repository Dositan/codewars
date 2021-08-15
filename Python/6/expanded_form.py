
def expanded_form(num):
    result = []
    divider = 10
    while divider < num:
        temp = num % divider
        if temp != 0:
            result.insert(0, str(temp))
        num -= temp
        divider *= 10
    result.insert(0, str(num))
    return ' + '.join(result)


print(expanded_form(70304))