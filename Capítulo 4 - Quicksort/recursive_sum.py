def sum(array):
    if array == []:
        return 0
    return array[0] + sum(array[1:])

array = [2,4,6]

print(sum(array))