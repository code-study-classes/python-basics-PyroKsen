def square_odds(numbers):
    return [x ** 2 for x in numbers if x % 2 != 0]



def normalize_names(names):
    return [name.capitalize() for name in names]



def remove_invalid_emails(emails):
    valid_emails = []
    for email in emails:
        if (
            email.count('@') == 1 and
            len(email) >= 5 and
            not email.startswith('@') and
            not email.endswith('@')
        ):
            valid_emails.append(email)
    return valid_emails



def filter_palindromes(words):
    palindromes = []
    for word in words:
        normalized_word = word.lower()
        if normalized_word == normalized_word[::-1]:
            palindromes.append(word)
    return palindromes
    


def calculate_factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial



def find_common_prefix(strings):
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
    return prefix