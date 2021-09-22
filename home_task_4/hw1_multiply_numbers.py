
"""

    1.	Multiply numbers with regex.

Дан текст:
Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира,
только у троих футболистов средний показатель превышает 2 гола за игру.
Эти 35 игроков представляют 14 футбольных сборных.

Напишите функцию которая умножает каждую цифру в тексте на 2, и возвращает изменённый текст

Примечания:
•	используйте re.sub https://docs.python.org/3/library/re.html#re.sub
•	обратите внимание на параметр repl (repl can be a string or a function)

"""


import re


def multiply_nums(text, multiplier=2):
    """

    >>> multiply_nums('I am 10 years old')
    'I am 20 years old'

    >>> multiply_nums('I am 10 years old', multiplier=25)
    'I am 250 years old'

    """
    numRegex = re.compile(r'[\d]+')
    multifunc = lambda matchobj: str(int(matchobj.group(0)) * multiplier)

    return numRegex.subn(multifunc, text)[0]


if __name__ == '__main__':
    text = "Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, " \
           "только у троих футболистов средний показатель превышает 2 гола за игру. " \
           "Эти 35 игроков представляют 14 футбольных сборных."
    print(multiply_nums(text))
