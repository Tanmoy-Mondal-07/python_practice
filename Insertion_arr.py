def insert_element(arr, element, position):

  if not 0 <= position <= len(arr):
    raise ValueError("Invalid position")

  if position == 0:
    return [element] + arr
  elif position == len(arr):
    return arr + [element]
  else:
    return arr[:position] + [element] + arr[position:]

arr = [1, 2, 3, 4, 5, 6, 7]
element = int(input("Enter an element to insert: "))
position = int(input("Enter the position (0 to insert at the beginning): "))

try:
  new_arr = insert_element(arr, element, position)
  print("New array:", new_arr)
except ValueError as e:
  print(e)
