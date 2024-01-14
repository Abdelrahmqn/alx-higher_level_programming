#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for i, specific_character in enumerate(str):
        if i != n:
            result = result + specific_character
    return result
