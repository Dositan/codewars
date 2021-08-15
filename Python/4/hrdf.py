"""Human Readable Duration Format."""

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
YEAR = DAY * 365

formats = (
    (YEAR, 'year'),
    (DAY, 'day'),
    (HOUR, 'hour'),
    (MINUTE, 'minute'),
    (1, 'second'),
)


def plural(amount: int, word: str) -> str:
    return f"{amount} {word}{'s' if amount != 1 else ''}"


def format_duration(seconds: int) -> str:
    result = []
    for period, word in formats:
        if seconds >= period:
            n = int(seconds / period)
            result.append(plural(n, word))
            seconds -= n * period
    return ' and'.join(', '.join(result).rsplit(',', 1))
