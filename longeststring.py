def find_longest_string(my_list):
    longest = ''
    for i in my_list:
        if len(i)>len(longest):
            longest = i
        
    return longest    


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""