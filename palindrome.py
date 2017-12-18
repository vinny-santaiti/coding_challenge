
def find_longest_palindromic_string(text):
    """ Manacher's Algorithm - finds longest contiguous palindromic substring """
    n = len(text)
    start = 0
    max_len = 1
    matrix = [[False for _ in range(n)] for _ in range(n)]
    # all palindrome of length 1
    for i in range(n):
        matrix[i][i] = True
    # check palindrome of length 2
    for i in range(n-1):
        if text[i] == text[i + 1]:
            matrix[i][i + 1] = True
            start = i
            max_len = 2
    # check palindrome of length 3 or more
    for length in range(3, n):
        for i in range(n-length+1):
            j = i + length - 1
            if text[i] == text[j] and matrix[i+1][j-1]:
                matrix[i][j] = True
                start = i
                max_len = length
    return text[start: start + max_len]

s = "Ilikeracecarsthatgofast"
assert find_longest_palindromic_string(s) == "racecar"

long_string = """FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo
ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto
getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco
nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobed
edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore
ddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod
shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"""
assert find_longest_palindromic_string(long_string) == "ranynar"
