# P: go through string and check if all characters are unique
# input - string
# output - boolean

# Ex:
# "aabc" - false
# "abc" - true
# "Ahn" - true
# " " - none

# D:
# Dictionaries

# A:
# 0. if length of input string is 0, return none
# 1. Create a list of chars 
# 2. Loop over chars. For each character 
#   1. if char in chars 
#         return False
#     2. else set char = 1
# 3. return true

def unique_chars(str):
    charLis = list(str.split(''))
    count = 1
    charDic = {}
    for i in charLis:
        if i in charDic:
            return 'false'
        else 
    