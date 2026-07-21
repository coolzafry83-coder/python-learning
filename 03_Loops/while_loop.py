# While Loop Practice

# Counting 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1


print("----")


# Countdown 10 to 1
number = 10

while number >= 1:
    print(number)
    number -= 1


print("----")


# Even Numbers
num = 2

while num <= 10:
    print(num)
    num += 2


print("----")


# Break Example
count = 1

while count <= 10:
    print(count)

    if count == 5:
        break

    count += 1


print("----")


# Continue Example
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)