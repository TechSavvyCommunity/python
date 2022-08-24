# Loops

In general, statements are executed sequentially: The first statement in a function is executed first, followed by the second, and so on. There may be a situtation when you need to execute a block of code several number of times. <br>
Programming language provides various control structures that allow for more complicated execution paths. <br>
<b>A loop statement allows us to execute a statement or group of statements mutliple times.</b> <br>
Python provides following types of loops to handle looping requirements.
| S.No. | Loop Type | Description |
| :---: | :---: | :---: |
| 1.  | while loop  | It repeats a statement or group of statements while a given condition is TRUE. it tests the condition before executing the loop body  |
| 2.  | for loop  | It executes a sequence of statements multiple times and abbreviates the code that manages the loop variable |
| 3.  | nested loop | It helps in using one or more loop inside any other while, for or while loop. | 

### NOTE
<b>Python does not support do...while loop, which in general is supported by other programming languages. </b>

## Syntax
### While loop
```md
declaration

while(condition):
  statement 1
  statement 2
  .
  .
  .
  statement n
  
  increment / decrement
```
#### Example
```md
i = 0
while i <= 10:
  print(i)
  
  i += 1
```
