import hashlib

with open("security_file.txt", "rb") as file:
    data = file.read()

current_hash = hashlib.sha256(data).hexdigest()

original_hash = "6f0b2f8efad8b0424676e41706ac40b869fa35b94b389511288d601145a6afd7"

if current_hash == original_hash:
    print("File is safe.")
else:
    print("Warning! File has been modified.")