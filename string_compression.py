"""	string compression 
http://www.zlib.net/ 
better than run length encoding
"""
import base64
import zlib 

def encode(data):
    code = zlib.compress(data)
    code = base64.encodestring(code)
    return code

def decode(code):
    code = base64.decodestring(code)
    data = zlib.decompress(code)
    return data

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
