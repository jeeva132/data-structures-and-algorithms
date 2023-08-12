def find_duplicates(list1):
    num_counts = {}
    
    for i in list1:
        if i not in num_counts:
            num_counts[i] = 1
        else:
            num_counts[i] +=1
    duplicates = [num for num,count in num_counts.items() if count>1]
        
    return duplicates


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )
