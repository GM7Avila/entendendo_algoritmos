def count(array):
    
    if array == []:
        return 0
    
    return 1 + count(array[1:])

array = [2,4,6]

print(count(array))