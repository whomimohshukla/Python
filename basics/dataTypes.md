# Data Types in Python

- Python is a dynamically typed language.
- It means that the type of a variable is determined at runtime.
- The type of a variable is determined by the value assigned to it.
- The type of a variable can be changed at runtime.

## Data Types

| Data Type | Description |
| --- | --- |
| Integer | A whole number, such as 1, 2, 3, etc.
| Float | A decimal number, such as 1.0, 2.5, 3.14, etc.
| String | A sequence of characters, such as "Hello", "World", etc.
| Boolean | A logical value, either True or False.
| List | An ordered collection of items, such as [1, 2, 3, 4, 5].
| Tuple | An ordered collection of items, such as (1, 2, 3, 4, 5).
| Dictionary | An unordered collection of key-value pairs, such as {"name": "John", "age": 30}.

- set : An unordered collection of unique items.


-File : A sequence of characters that can be read or written to a file.

-None : A special value that indicates the absence of a value.

## Data Type Conversion

- Converting data types is a process of changing the data type of a variable from one type to another.
- Python provides built-in functions for converting data types.
- The built-in function for converting data types is called type conversion.

### Type Conversion in Python

| Data Type | Built-in Function |
| --- | --- |
| Integer | int() |
| Float | float() |
| String | str() |
| Boolean | bool() |
| List | list() |
| Tuple | tuple() |
| Dictionary | dict() |

### Type Conversion Examples

```python
# Converting Integer to Float
x = 10
y = float(x)
print(y)  # Output: 10.0

# Converting Float to Integer
x = 10.5
y = int(x)
print(y)  # Output: 10

# Converting String to Integer
x = "10"
y = int(x)
print(y)  # Output: 10

# Converting String to Float
x = "10.5"
y = float(x)
print(y)  # Output: 10.5

# Converting String to Boolean
x = "True"
y = bool(x)
print(y)  # Output: True
```

## Type Conversion Errors

- Type conversion errors occur when the built-in function for converting data types fails to convert the data type.
- Type conversion errors can occur when the input data is not in the correct format or when the input data is not of the expected type.
- Type conversion errors can also occur when the input data is not in the correct range or when the input data is not of the expected type.

### Type Conversion Errors Examples

```python
# Type Conversion Error: Input data is not in the correct format
x = "abc"
y = int(x)
print(y)  # Output: ValueError: invalid literal for int() with base 10: 'abc'

# Type Conversion Error: Input data is not of the expected type
x = 10.5
y = str(x)
print(y)  # Output: ValueError: invalid literal for str() with base 10: 10.5

# Type Conversion Error: Input data is not in the correct range
x = 10
y = str(x)
print(y)  # Output: '10'
```

## Type Conversion Best Practices

- When converting data types, it is important to consider the expected input data and the expected output data.
- It is also important to check the input data for errors and to handle them appropriately.
- It is also important to check the output data for errors and to handle them appropriately.

### Type Conversion Best Practices Examples

```python
# Type Conversion Best Practice: Checking the input data for errors
x = "abc"
y = int(x)
if y == ValueError:
    print("Input data is not in the correct format")
else:
    print(y)

# Type Conversion Best Practice: Handling errors appropriately
x = "abc"
y = int(x)
try:
    print(y)
except ValueError:
    print("Input data is not in the correct format")

# Type Conversion Best Practice: Checking the output data for errors
x = 10.5
y = str(x)
if y == ValueError:
    print("Input data is not in the correct format")
else:
    print(y)

# Type Conversion Best Practice: Handling errors appropriately
x = 10.5
y = str(x)
try:
    print(y)
except ValueError:
    print("Input data is not in the correct format")
```

## Type Conversion in Real-World Applications

- Type conversion is commonly used in real-world applications to convert data from one format to another.
- For example, when working with databases, type conversion is often used to convert data from one format to another.
- Type conversion is also commonly used in web development to convert data from one format to another.
- Type conversion is also commonly used in data analysis to convert data from one format to another.

### Type Conversion in Real-World Applications Examples

```python
# Type Conversion in Real-World Applications: Converting data from one format to another
# Example 1: Converting data from one format to another
x = 10.5
y = str(x)
print(y)  # Output: "10.5"

# Example 2: Converting data from one format to another
x = "10.5"
y = float(x)
print(y)  # Output: 10.5

# Example 3: Converting data from one format to another
x = "True"
y = bool(x)
print(y)  # Output: True

# Example 4: Converting data from one format to another
x = [1, 2, 3, 4, 5]
y = tuple(x)
print(y)  # Output: (1, 2, 3, 4, 5)

# Example 5: Converting data from one format to another
x = {"name": "John", "age": 30}
y = dict(x)
print(y)  # Output: {"name": "John", "age": 30}
```

## Summary

- Data types are an essential part of programming.
- Python provides built-in functions for converting data types.             