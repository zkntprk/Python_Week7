# Write a program that detects the ID number hidden in a text.
# We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit
# (For example: AA4ZA11B1). 9digit total!?
#
# Input : AABZA1111AEGTV5YH678MK4FM53B6
#
# Output : MK4FM53B6
#
# Input : AEGTV5VZ4PF94B6YH678
#
# Output : VZ4PF94B6

import re

def in_out():
    with open('hiddenID.txt', 'a', encoding="utf-8") as file:
        text = file.read()
        pattern = r'\w{2}\d\w{2}\d{2}\w\d'
    return print('Founded hidden ID list: ', re.findall(pattern, text))


def findhiddenID():
    with open('hiddenID.txt', 'r', encoding="utf-8") as file:
        text = file.read()
        pattern = r'\w{2}\d\w{2}\d{2}\w\d'
    return print('Founded hidden ID list: ' ,re.findall(pattern, text))


findhiddenID()
