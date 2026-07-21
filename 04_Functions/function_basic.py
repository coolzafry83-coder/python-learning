# Basic Function

def say_hello():
    print("Hello Muhammad")

say_hello()


print("----")


# Function with Parameter

def greet(name):
    print("Hello", name)

greet("Muhammad")
greet("Ali")


print("----")


# Function with Multiple Parameters

def add_numbers(a, b):
    result = a + b
    print(result)

add_numbers(5, 3)


print("----")


# Function with Return

def multiply(a, b):
    return a * b

answer = multiply(4, 5)

print(answer)


print("----")


# Real Example

def calculate_total(price, quantity):
    total = price * quantity
    return total

bill = calculate_total(500, 3)

print("Total Bill:", bill)