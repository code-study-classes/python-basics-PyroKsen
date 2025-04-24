def check_between_numbers(A, B, C):
    return (lambda a, b, c: a < b < c or c < b < a)(A, B, C)


def check_odd_three(number):
    return (lambda n: (100 <= abs(n) <= 999) and (n % 2 != 0))(number)


def check_unique_digits(number):
    is_three_digit = (lambda n: 100 <= abs(n) <= 999)(number)
    if not is_three_digit:
        return False
    
    unique_check = (lambda digits: len(set(digits)) == len(digits))
    digits = str(abs(number))
    return unique_check(digits)


def check_palindrome_number(number):
    str_num = str(abs(number))
    is_palindrome = (lambda s: s == s[::-1])(str_num)
    return is_palindrome
    


def check_ascending_digits(number):
    if not (100 <= abs(number) <= 999):
        return False

    digits = str(abs(number))
    is_ascending = (lambda d: all(d[i] < d[i + 1] for i in range(len(d) - 1)))(digits)
    return is_ascending