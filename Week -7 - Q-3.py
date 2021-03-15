# #
# Write a program that list according to email addresses without email domains in a text.
#
# Example:
#
# Input:
#
# The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com.
# Then New Yorker article on wind farms...
#
# Output :
#
# franky
#
# sinatra123

import re

with open('mailtext.txt', 'r', encoding="utf-8") as file:
    text = file.read()
    pattern = r'\S+@'
    lst = re.findall(pattern, text)
    new_lst = []

    for i in range(len(lst)):
        new_lst.append(lst[i][:-1])
        print(new_lst[i])
