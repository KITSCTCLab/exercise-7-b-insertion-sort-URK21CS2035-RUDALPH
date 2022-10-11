from typing import List

def selectionSort(arr, size) -> List[int]:
  # Write your code here
  for i in range(size):
    min = i
    for j in range(i + 1, size):
      if arr[min] > arr[j]:
        min = j;
    arr[i], arr[min] = arr[min], arr[i]
  return arr

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
