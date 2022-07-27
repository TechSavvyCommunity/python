# Variables
Variables are the reserved memory locations to store values. This means that when you create a variable you reserve some space in memory. <br>
Based on data types of variable, the interpreter allocates memory and decides what can be stored in the reserved memeory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.

## Assigning Values to Variables
Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables. <br>
The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value to be stored in the variable. For example:
```md
number_value = 100                      # an integer assignment
floating_value = 99.99                  # a floating point
string_value = "TechSavvyCommunity"     # a string
print(number_value)
print(floating_value)
print(string_value)
```
Here, 100, 99.99 and TechSavvyCommunity are the values assigned to number_value, floating_value and string_value variables respectively. This produces the following result:
```md
100
99.29
TechSavvyCommunity
```

## Multiple Assignment
Python allows you to assign a single value to several variables simultaneously. For example:
```md
x = y = z = 100
print(z)
```
Here, an integer object is created with the value 100, and all three variables are assigned to the same memory location. You can also assign multiple objects to multiple variables. For example:
```md
x, y, z = 100, 500, 1000
print(z)

# OUTPUT: 1000
```
