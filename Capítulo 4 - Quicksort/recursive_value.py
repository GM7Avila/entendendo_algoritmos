# Encontre o valor mais alto em uma lista

def max(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = max(array[1:])
    return array[0] if array[0] > sub_max else sub_max

array = [2,4,6]

print(max(array))