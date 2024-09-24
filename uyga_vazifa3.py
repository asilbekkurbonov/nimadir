def count_elements(lst):
    
    element_count = {}
    
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    return element_count

myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]

myDct = count_elements(myList)
print(myDct)