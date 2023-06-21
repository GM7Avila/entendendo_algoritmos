def findSmallest(array):
  smallest = array[0]
  smallest_index = 0
  for i in range(1, len(array)):
    if array[i] < smallest:
      smallest_index = i
      smallest = array[i]      
  return smallest_index


def selectionSort(array):
  newArray = []
  for i in range(len(array)):
      smallest = findSmallest(array)
      newArray.append(array.pop(smallest))
  return newArray

print(selectionSort([5, 3, 6, 2, 10]))