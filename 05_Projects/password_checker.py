def check_length(password):
    return len(password) >= 8


def check_number(password):
    for character in password:
        if character.isdigit():
            return True
    return False


def check_uppercase(password):
    for character in password:
        if character.isupper():
            return True
    return False


def check_lowercase(password):
    for character in password:
        if character.islower():
            return True
    return False


def check_special(password):
    for character in password:
        if character in "@#$%!&":
            return True
    return False


# Main Program

password = input("Enter your password: ")

score = 0

if check_length(password):
    print("Good Length")
    score += 1
else:
    print("Weak Length")


if check_number(password):
    print("Password contains a number")
    score += 1
else:
    print("Password does not contain a number")


if check_uppercase(password):
    print("Password contains uppercase")
    score += 1
else:
    print("Password does not contain uppercase")


if check_lowercase(password):
    print("Password contains lowercase")
    score += 1
else:
    print("Password does not contain lowercase")


if check_special(password):
    print("Password contains special character")
    score += 1
else:
    print("Password does not contain special character")


# Final Strength

if score == 5:
    print("Password Strength: Strong")
elif score >= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")