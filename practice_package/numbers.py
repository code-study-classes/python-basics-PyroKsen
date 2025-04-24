def calculate_distance(x, y):
    return (lambda a, b: abs(a - b))(x, y)


def calculate_segments(a, b):
    return (lambda a, b: a // b)(a, b)


def calculate_digit_sum(number):
    return (lambda n: sum(int(digit) for digit in str(abs(n))))(number)


def round_to_multiple(number, multiple):
    return (lambda n, m: round(n / m) * m)(number, multiple)
    


def calculate_rect_area(x1, y1, x2, y2):
    return (lambda x1, y1, x2, y2: abs(x2 - x1) * abs(y2 - y1))(x1, y1, x2, y2)