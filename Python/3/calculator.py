import operator


class Calculator:
    operands = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    @classmethod
    def __calculate(cls, i, char, strings):
        a = float(strings[i - 1])
        b = float(strings[i + 1])
        strings[i] = str(cls.operands[char](a, b))

        del strings[i + 1], strings[i - 1]

    def __process_expr(self, string: str, operators: list) -> str:
        strings = string.split()
        while any((True if s in operators else False) for s in strings):
            for i, char in enumerate(strings):
                if char in operators:
                    self.__calculate(i, char, strings)
                    break
        return ' '.join(strings)

    def evaluate(self, string: str):
        string = self.__process_expr(string, ("*", "/"))
        result = self.__process_expr(string, ("+", "-"))
        return float(result)


calc = Calculator()
assert calc.evaluate("123 * 2") == 246
# assert calc.evaluate("( ( ( ( 1 ) * 2 ) ) )")
