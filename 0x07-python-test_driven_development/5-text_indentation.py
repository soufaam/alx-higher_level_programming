#!/usr/bin/python3

""" This is a decription of this module .

This module contains a function called text_indentation
that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over
multiple lines. Sections are created
with a section header and a colon followed
by a block of indented text.
"""


def text_indentation(text):
    """a function that adds 2 integers.
    Prototype: def text_indentation(text):
    args:
    text: must be strings
    A function that prints My name is <first name> <last name>"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        if letter == '.' or letter == '?' or letter == ':':
            print(f"{letter}\n")
            continue
        print(letter, end='')
