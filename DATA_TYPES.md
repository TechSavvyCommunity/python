# Data Types
The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his/her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them. <br>
Python has five standard data types - <br>
* Numbers       <br>
* String        <br>  
* List          <br>
* Tuple         <br>
* Dictionary    <br>

# Python Numbers
Number data types store numeric values. Number objects are created when you assign a value to them. For example:
```md
num1 = 100
num2 = 200.222
```
* Python supports four different numerical types: <br>
&emsp; 1. int (signed integers) <br>
&emsp; 2. long (long integers, they can also be represented in octal and hexadecimal) <br>
&emsp; 3. float (floating point real values) <br>
&emsp; 4. complex (complex numbers)

## Examples:
Here are some examples of numbers: <br>
| INT | LONG | FLOAT | COMPLEX |
| :---: | :---: | :---: | :---: |
| 10 | 51924361L | 0.0 | 3.14j |
| 100 | -0x19323L | 15.20 | 45.j |
| -786 | 0122L | -21.9 | 9.322e-36j |
| 080 | 0xDEFABCECBDAECBFBAEI | 32.3+e18 | .876j |
| -0490 | 535633629843L | -90. | -.6545+0J |
| -0x260 | -4721885298529L | 70.2-E12 | 4.53e-7j |

* Python allows you to use lowercase l with long, but it is recommended that you use only an uppercase L to avoid confusion with number 1. Python displays long integers with an uppercase L. <br>
* A complex number consists of an ordered pair of real floating-point number denoted by x + yj, where x and y are the real number and j is the imaginary unit.

# Python Strings
Strings in Python are defined as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice operator ([] and [:]) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end. <br>
The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator. For example:
```md
str = 'Hello World!'
print(str)              # Prints complete string
print(str[0])           # Prints first character of the string
print(str[2:5])         # Prints character starting from 3rd to 5th (i.e., index 2 to index 4)
print(str[2:])          # Prints string starting from 3rd character 
print(str * 2)          # Print string two times
print(str + "test")     # Prints concatenated string
```

This will produce the following result:
```md
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!test
```

# Python Lists
Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type. <br>
The values sorted in a list can be accessed using the slice operator ([] and [:]) with indexes starting at 0 in the beginnnig of the list and working their way to end -1. The plus (+) sign is the concatenation operator, and the asterisk (*) is the repetition operator. For example:
```md
list = ['ANUJ', 100, 500, 1000]
small_list = [786, 'Python']
print(list)                       # Prints comlete list
print(list[0])                    # Prints first element of the list
print(list[1:3])                  # Prints elements starting from 2nd till 3rd
print(list[2:])                   # Prints elements starting from 3rd element
print(small_list * 2)             # Prints small_list two times
print(list + small_list)          # Prints concatenated lists
```

This produce the following result -
```md
['ANUJ', 100, 500, 1000]
ANUJ
[100, 500]
[500, 1000]
[786, 'Python', 786, 'Python']
['ANUJ', 100, 500, 1000, 786, 'Python']
```

# Python Tuples
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parenteses. <br>
The main differences between lists and tuples are: Lists are enclosed in brackets ([]) and their elements and size can be changed, while tuples are enclosed in parentheses (()) and cannot be updated. Tuples can be thought of as read-only lists. For example:
```md
tuple = ('ANUJ', 100, 500, 1000)
small_tuple = (786, 'Python')
print(tuple)                    # Prints complete tuple
print(tuple[0])                 # Prints first elements of the tuple
print(tuple[1:3])               # Prints element starting from 2nd till 3rd
print(tuple[2:])                # Prints elements starting from 3rd elements
print(small_tuple * 2)          # Prints small_tuple two times
print(tuple + small_tuple)      # Prints concatenated tuples
```

This produce the following result - <br>
```md
('ANUJ', 100, 500, 1000)
ANUJ
(100, 500)
(500, 1000)
(786, 'Python', 786, 'Python')
('ANUJ', 100, 500, 1000, 786, 'Python')
```


