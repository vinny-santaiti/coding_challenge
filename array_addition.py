""" 
array_addition

[1,2,3] -> [1,2,4]
[9,9,9] -> [1,0,0,0]
"""
def add_one(array):
    carry=1
    index = 0
    for x in range(len(array)):
        index+=-1
        number = array[index]
        print number
        if number == 9:
            array[index]=0
        else:
            array[index]=number+1
            carry=0
            break
    if carry==1:
        new_arr = [1]
        new_arr.extend(array)
        return new_arr
    return array

print add_one([1,2,3])

print add_one([1,9,9])

print add_one([9,9,9])
