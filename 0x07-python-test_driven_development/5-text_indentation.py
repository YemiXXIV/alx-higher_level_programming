#!/usr/bin/python3
"""

Prints text with 2 new lines after each '.', '?', and ':' characters.

"""


def text_indentation(text):
    """
    Module for text indentation.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    length = len(text)
    i = 0
    while (i < length):
        if text[i] in (".", "?", ":"):
            if (i + 1) != length:
                j = text[i + 1]
                if (j != '.' and j != '?' and j != ':'):
                    print(text[i], end='\n\n')
                    if j == ' ':
                        i += 2
                    if j != ' ':
                        i += 1
        else:
            print(text[i], end='')
            i += 1
