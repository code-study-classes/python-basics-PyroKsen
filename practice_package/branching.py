def is_weekend(day):
    return day == 6 or day == 7

def get_discount(amount):

    discount_mapping = {
        5000: 0.10,
        1000: 0.05
    }

    discount_rate = next((rate for threshold, rate in discount_mapping.items() if amount >= threshold), 0)
    return round(amount * discount_rate, 2)

def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    match n:
        case _ if n < 10:
            digits = "однозначное"
        case _ if n < 100:
            digits = "двузначное"
        case _:
            digits = "трехзначное"

    return f"{parity} {digits} число"

def convert_to_meters(unitNumber, lengthInUnits):
    conversion_factors = {
        1: 0.1,     # дециметр
        2: 1000,    # километр
        3: 1,       # метр
        4: 0.001,   # миллиметр
        5: 0.01     # сантиметр
    }

    conversion_factor = conversion_factors.get(unitNumber)
    return lengthInUnits * conversion_factor

def describe_age(age):
    if age == 100:
        return 'сто лет'

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", 
             "семьдесят", "восемьдесят", "девяносто"]

    ten = age // 10
    unit = age % 10
    age_in_words = f"{tens[ten]} {units[unit]}".strip()

    if age % 10 == 1 and age % 100 != 11:
        suffix = "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        suffix = "года"
    else:
        suffix = "лет"

    return f"{age_in_words} {suffix}"