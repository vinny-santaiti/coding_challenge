""" string compression
    Encode a string to as short a length as possible then decode it
"""

def encode(string):
    """string compress: "aaab" to "a3b" """
    last = string[0]
    result = []
    count = 1
    for char in string[1:]:
        if char == last:
            count += 1
        else:
            if count == 1:
                result.append(last)
            else:
                result.append('{}{}'.format(last, count))
            count = 1
            last = char
    if count == 1:
        result.append(last)
    else:
        result.append('{}{}'.format(last, count))
    return ''.join(result)

def decode(string):
    """restore original string: a4b = aaaab"""
    result = []
    string = list(string)
    for i, x in enumerate(string):
        if x.isdigit():
            result.append(string[i-1]*int(x)) 
        elif i != 0 and string[i-1] != x and string[i-1].isalpha():
            result.append(string[i-1])
    if x.isalpha():
        result.append(x) 
    return ''.join(result) 

# Run length encoding "aaaabbaaa" -> "4a2b3a"
strings = [
'0DE9MDK9J8I1BMUQ18HARUPOKXFE4HLADWV12OYYTUFI59Y1', # 47
'6QXXCOLMUNBLYY0WOB5BR2HIR5L5XG02TGRAGV', # 36
'5PNL', # 4
'GKF8ANZ2DH6P3B5WWFMELX8XEMRSJGKHMDN932EZTM2O', # 43
'4ZILNB9DW3Y65GIG4Z5WWICIJN6H7HTU88', # 32
'Aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa', # 12
'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW' # 14
]
for string in strings:
    assert decode(encode(string)) == string