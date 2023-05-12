# PythonLearnings

# ** Cheat Sheet **

## Sequence of Instructions

### Program

A program is a sequence of instructions given to a computer.

## Defining a Variable

A variable gets created when you assign a value to it for the first time.

Code

```
age = 10
```

## Printing Value in a Variable

Code

```
age = 10
print(age)
```

Output

```
10
```

Code

```
age = 10
print("age")
```

Output

```
age
```

Variable name enclosed in quotes will print variable rather than the value in it.
If you intend to print value, do not enclose the variable in quotes.

# Order of Instructions

Python executes the code line-by-line.

Code

```
print(age)
age = 10
```

Output

```
NameError: name 'age' is not defined
```

Variable age is not created by the time we tried to print.

## Spacing in Python

Having spaces at the beginning of line causes errors.

Code

```
a = 10 * 5
b = 5 * 0.5
 b = a + b
```

Output

```
File "main.py", line 3
    b = a + b
    ^
IndentationError: unexpecte
```

## Variable Assignment

Values in the variables can be changed.

Code

```
a = 1
print(a)
a = 2
print(a)
```

Output

```
1
2
```

### ** Examples of Variable Assignment **

Code

```
a = 2
print(a)
a = a + 1
print(a)
```

Output

```
2
3
```

Code

```
a = 1
b = 2
a = b + 1
print(a)
print(b)
```

Output

```
3
2
```

## Expression

An expression is a valid combination of values, variables and operators.

Examples
a _ b
a + 2
5 _ 2 + 3 \* 4

### ** BODMAS **

The standard order of evaluating an expression

- Brackets (B)
- Orders (O)
- Division (D)
- Multiplication (M)
- Addition (A)
- Subtraction (S)

* Step by Step Explanation \*

(5 _ 2) + (3 _ 4)
(10) + (12)
22

Code

```
print(10 / 2 + 3)
print(10 / (2 + 3))
```

Output

```
8.0
2.0
```
