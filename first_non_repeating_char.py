def first_non_repeating_char(string):
    dict1 = {}
    for i in string:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] +=1
    
    for i in dict1:
        if dict1[i] ==1:
            return i
    return None

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""