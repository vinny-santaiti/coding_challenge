# longest_palindromic_substring

# for string csadfbabsdasd, the answer is bab
# for bab, the answer is bab
# for bac, the answer is null

def longest_palindromic_substring(my_str):
    # the solution is a dynamic problem
    # the left lower half of table (triangle) is always false or zero
    matrix = [[0 for x in range(len(my_str))] for y in range(len(my_str))]
    # print matrix
    # which is equiv to:
    """
    matrix = range(len(my_str))
    for x in range(len(my_str)):
        matrix[x] = [0] * len(my_str)
    """
    # since a palindrome of length 1 is always a palindrome
    for x in range(len(my_str)):
        matrix[x][x] = 1
    # length 2, if char is same as first then True
    for x in range(len(my_str)-1): 
        if my_str[x] == my_str[x+1]:    
            matrix[x][x+1] = 1
    """
    need to loops over all combinations of string
    for my_str = "aba", increaseing in length from 1 to length of string
    a
    b
    a
    ab
    ba
    aba
    """
    palindrome_length = 0
    palindrome = ""
    for y in range(1, len(my_str)): # this increases length of string
        # print y
        for i in range(len(my_str)-y): # this is for looking at chars in string
            j=i+y
            # print i, j, my_str[i:j] 
            if my_str[i] == my_str[j] and matrix[i+1][j-1] == 1:    
                matrix[i][j] = 1
                if len(my_str[i:j]) > palindrome_length:
                    palindrome = my_str[i:j+1] # since the last char should be added
                    palindrome_length = len(palindrome)
                    # print 'palindrome', palindrome
        # print matrix
    return palindrome

my_str = "catlolasdsarob"
print longest_palindromic_substring(my_str)
