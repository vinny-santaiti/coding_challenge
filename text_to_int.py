"""python translate words to integers"""


def text_to_num(words):
    """convert words to single number, twenty nine = 29"""
    is_negative = False
    if "negative" in words:
        words = words.replace('negative', '').strip()
        is_negative = True
    units = [
      "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
      "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
      "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    wordmap = {}
    for index, word in enumerate(units):
        wordmap[word] = index
    for index, word in enumerate(tens):
        wordmap[word] = index * 10
    for index, word in enumerate(scales):
        wordmap[word] = 10 ** (index * 3 or 2)
    result = 0
    current = None
    for word in reversed(words.split()):
        if word not in wordmap:
            raise Exception(word + " not valid")
        if current:
            result += wordmap[word] * current
            current = None
        elif word in units or word in tens:
            result += wordmap[word]
        else:
            current = wordmap[word]
    if is_negative:
        result = -result
    return result

assert text_to_num("negative seven hundred twenty nine") == -729
assert text_to_num("one million one hundred one") == 1000101
assert text_to_num("one thousand five hundred") == 1500
text_to_num("boo")  # raises exception
