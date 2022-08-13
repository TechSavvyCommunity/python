# Operators
Operators are the symbols that tells the computer to perform specific manipulations.

## Types of Operators
Python supports the following types of operators:
* Arithmetic Operators
* Comparison (Realtional) Operators
* Assignment Operators
* Logical Operators
* Bitwise Operators
* Membership Operators
* Identity Operators

### Arithmetic Operators
**An arithmetic operators are used with numeric values to perform common mathematical operations.** <br>
Assume variable a = 20 and b = 30, then: <br>
| S.No. | Operator | Name  | Description | Example |
| :---: | :---: | :---: | :---: | :---: |
| 1.  | + | Addition  | Adds values on either side of the operator  | a + b = 50 |
| 2.  | - | Subtraction | Subtracts right hand operand from left hand operand | a - b = -10 |
| 3.  | * | Multiplication  | Multiplies values on either side of the operator  | a * b = 600 |
| 4.  | / | Division  | Divides left hand operand by right hand operand | b / a = 1.5 |
| 5.  | % | Modulus | Divides left hand operand by right hand operator and returns remainder  | b % a = 10  |
| 6.  | **  | Exponent  | Performs exponential (power) calculation on operators | a ** b = 20 to the power 30 |
| 7.  | //  | Floor Division  | The division of operands where the result is the quotient in which the digits after the decimal points are removed. But if one of the operand is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) |  9 // 2 = 4 and 9.0 // 2.0 = 4.0, -11 // 3 = -4, -11.0 / /3 = -4.0 |
<br>
Click on 👉 <a href="https://github.com/bishtanuj/python/tree/main/Operators#arithmetic-operators">Programs</a> for more practical approach.

## Comparison Operators
**These operators compare the values on either sides of them and decide the relation among them. They are also called relational operators.** <br>
Assume variable a = 20 and b = 30, then: <br>
| S.No. | Operator | Name  | Description | Example |
| :---: | :---: | :---: | :---: | :---: |
| 1.  | ==  | Equal | If the values of two operands are equal, then the condition becomes true. | (a == b) is not true  |
| 2.  | !=  | Not Equal | If values of two operands are not equal, then the condition becomes true. | (a != b) is true  |
| 3.  | > | Greater Than  | If the value of the left operand is greater, than the the value of right operand, then the condition becomes true. |  (a > b) is not true |
| 4.  | < | Less Than | If the value of the left operand is less, than the value of right operand, then the condition becomes true. | (a < b) is true |
| 5.  | >=  | Greater Than or Equal To  | If the value of the left operand is greater than or equals to the value of the right operand, then the condition becomes true.  | (a >= b) is not true. |
| 6.  | <=  | Less Than or Equal To | If the value of the lest operand is less than or equals to the value of the right operand, then the condition becomes true. | (a <= b) is true  |
<br>
Click on 👉 <a href="https://github.com/bishtanuj/python/tree/main/Operators#comparison-operators">Programs</a> for more practical approach.

## Assignment Operators
Assume variable a = 20 and b = 30, then: <br>
| S.No. | Operator  | Description | Example |
| :---: | :---: | :---: | :---: |
| 1.  | = | Assign values from right side operands to left side operand | (c = a + b) assigns value of a + b into c |
| 2.  | + =  | It adds right operand to teh left operand and assign the result to the left operand | c += a is equivalent to c = c + a |
| 3.  | - =  | It subtracts right operand from the left operand and assign the result to the left operand  | c -= a is equivalent to c = c - a |
| 4.  | * =  | It multiplies right operand with the left operand and assign the result to the left operand | c * = a is equivalent to c = c * a |
| 5.  | / =  | It divides the left operand with the right operand and assign the result to the left operand  | c /= a is equivalent to c = c / a |
| 6.  | % =  | It takes modulus using two operands and assign the result to left operand | c %= a is equivalent to c = c % a |
| 7.  | * * = | Performs exponential (power) calculation on operators and assign values to the left operand | c * * = a is equivalent to c = c * * = a  |
| 8.  | // = |  It performs floor division on operators and assign value to the left operand  | c // = a is equivalent to c = c // a  |
<br>
Click on 👉 <a href="https://github.com/bishtanuj/python/tree/main/Operators#assignment-operators">Programs</a> for more practical approach.

<!-- ## Bitwise Operators
**Bitwise operators works on bits and perform bit by bit operation. Let's assume a = 60 and b = 13; Now in binary format their values will be 00111100 and 00001101 respectively.** <br>
Therefore, here a = 00111100 and b = 00001101, then: <br>
| S.No. | Operator | Name  | Description | Example |
| :---: | :---: | :--- :  | :---: | :---: |
| 1.  | & | Binary AND  | Operator copies a bit to the result if it exists in both operands | (a & b) means 0000 1100 |
| 2.  | l | Binary OR | It copies a bit if it exists in either operand. | (a l b) = 61 means 0011 1101  |  -->
## Bitwise Operators
**Bitwise operators works on bits and perform bit by bit operation. Let's assume a = 60 and b = 13; Now in binary format their values will be 00111100 and 00001101 respectively.**  <br>
Therefore, here a = 00111100 and b = 00001101, then:
| S.No. | Operator | Name  | Description | Example |
| :---: | :---: | :---: | :---: | :---: |
| 1.  | & | AND | Sets each bit to 1 if both bits are 1 | |
| 2.  | l | OR | Sets each bit to 1 if one of the two bits is 1 | |
| 3.  | ^ | XOR | Sets each bit to 1 if only one of two bits is 1 | |
| 4.  | ~ | NOT | Inverts all the bits | |
| 5.  | << | Zero fill left shift | Shift left by pushing zeroes in form the right and let the leftmost bits fall of | |
| 6.  | >> | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall of | |

