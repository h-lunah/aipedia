"""Number generation functions"""

import random


def volume() -> str:
    """
    Generate a random volume number for the article.

    Returns:
        str: The roman numeral of the volume.
    """
    num = random.randint(1, 50)
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_numeral = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral


def page() -> int:
    """
    Generate a random page number for the article.

    Returns:
        int: The page number.
    """

    return random.randint(1, 1000)
