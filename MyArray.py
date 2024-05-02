from typing import TypeVar

T = TypeVar('T')  # Generic type variable

class CustomArray:
  def __init__(self, data_type: type, size: int) -> None:
    self.__data_type = data_type
    self.__size = size
    self.__data = [None] * size

  def __getitem__(self, index: int) -> T:
    if 0 <= index < self.__size:
      return self.__data[index]
    raise IndexError("Index out of bounds")

  def __setitem__(self, index: int, value: T) -> None:
    if 0 <= index < self.__size:
      if not isinstance(value, self.__data_type):
        raise TypeError(f"Expected data type {self.__data_type}, got {type(value)}")
      self.__data[index] = value
    else:
      raise IndexError("Index out of bounds")

  def __len__(self) -> int:
    return self.__size

# Example usage
my_int_array = CustomArray(int, 5)
my_int_array[0] = 10
my_string_array = CustomArray(str, 3)
my_string_array[1] = "Hello"
my_int_array[1]
print(my_int_array[0])  # Output: 10
print(my_string_array[1])  # Output: Hello

# Trying to set a wrong data type will raise an error
try:
  my_int_array[1] = "String"
except TypeError as e:
  print(e)  # Output: Expected data type <class 'int'>, got <class 'str'>
