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

### Comparison Operators
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

### Assignment Operators
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

### Bitwise Operators
**Bitwise operators works on bits and perform bit by bit operation. Let's assume a = 60 and b = 13; Now in binary format their values will be 00111100 and 00001101 respectively.**  <br>
Therefore, here a = 00111100 and b = 00001101, then:
| S.No. | Operator | Name  | Description | Example |
| :---: | :---: | :---: | :---: | :---: |
| 1.  | & | Binary AND  | Operator copies a bit to the result if it exists in both operands | (a & b) means 0000 1100 |
| 2.  | l | Binary OR | It copies a bit if it exists in either operand. | (a l b) = 61 means 0011 1101 |
| 3.  | ^ | XOR | It copies the bit if it is set in one operand but not both. |  (a ^ b) = 49 (means 0011 0001) |
| 4.  | ~ | NOT | It is unary and has the effect of 'flipping' bits. |  (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number. |
| 5.  | << | Binary left shift | The left operands value is moved left by the number of bits specified by the right operand. |  a << 2 = 240 (means 1111 0000) |
| 6.  | >> | Binary right shift | The left operands value is moved right by the number of bits specified by the right operand. |  a >> 2 = 15 (means 0000 1111) | 
<br>
Click on 👉 <a href="https://github.com/bishtanuj/python/tree/main/Operators#bitwise-operators">Programs</a> for more practical approach.

### Logical Operators
Assume variable a = 10 and b = 20, then: <br>
| S.No. | Operator  | Name  | Description | Example |
| :---: | :---: | :---: | :---: | :---: |
| 1.  | AND | Logical AND | If both the operands are true then condition becomes true.  | (a and b) is true |
| 2.  | OR  | Logical OR  | If any of the two operands are non-zero then condition becomes true.  | (a or b) is true  |
| 3.  | NOT | Logical NOT | Used to reverse the logical state of its operand. | Not(a and b) is false |
<br>
Click on 👉 <a href="https://github.com/bishtanuj/python/tree/main/Operators#logical-operators">Programs</a> for more practical approach.

### Membership Operators
**Membership operators are operators used to validate the membership of a value. It test for a membership in a sequence such as strings, lists or tuples.** 
| S.No. | Operator  | Description | Example |
| :---: | :---: | :---: | :---: |
| 1.  | in  | Evaluates to true if it finds a variable in the specified sequence and false otherwise. | x in y, here results in a 1 if x is a member of sequence y. |
| 2.  | not in  | Eveluates to true if it does not finds a variable in the specified sequence and false otherwise.  | x not in y, here not in results in a 1 if x is not a member of sequence y.  |
<br>
Click on 👉 <a href="https://github.com/bishtanuj/python/tree/main/Operators#membership-operators">Programs</a> for more practical approach.

### Identity Operators
**Identify operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.**
| S.No. | Operator  | Description | Example |
| :---: | :---: | :---: | :---: |
| 1.  | is  | Evaluates to true if teh variable on either side of the operator point tot eh same object and false otherwise.  | x is y, here is results in 1 if id (x) is equals to id (y) |
| 2.  | is not  | Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. | x is not y, here is not results in 1 if id (x) is not equal to id (y) |
<br>
Click on 👉 <a href="https://github.com/bishtanuj/python/tree/main/Operators#identity-operators">Programs</a> for more practical approach.

##
