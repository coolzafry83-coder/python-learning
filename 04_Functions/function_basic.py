# Python Functions Practice


# 1. Basic Function
def say_hello():
    print("Hello Muhammad")


say_hello()


print("----")


# 2. Function with Parameter
def greet(name):
    print("Hello", name)


greet("Muhammad")
greet("Ali")


print("----")


# 3. Multiple Parameters
def add_numbers(a, b):
    result = a + b
    print(result)


add_numbers(5, 3)


print("----")


# 4. Function with Return
def multiply(a, b):
    return a * b


answer = multiply(4, 5)

print(answer)


print("----")


# 5. Function with If Else
def check_number(number):
    if number > 0:
        print("Positive Number")
    elif number == 0:
        print("Zero")
    else:
        print("Negative Number")


check_number(5)
check_number(0)
check_number(-3)


print("----")


# 6. Function with Loop
def print_table(number):
    for i in range(1, 6):
        print(number, "x", i, "=", number * i)


print_table(5)


print("----")


# 7. Function with Condition and Loop
def check_even_numbers(limit):
    for number in range(1, limit + 1):
        if number % 2 == 0:
            print(number)


check_even_numbers(10)


print("----")


# 8. Default Parameter
def welcome(name="Guest"):
    print("Welcome", name)


welcome()
welcome("Muhammad")