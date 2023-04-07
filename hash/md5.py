import hashlib


# hash section
input_str = "cat" # <--- Replace with the string you want to hash
hashed_str = hashlib.md5(input_str.encode()).hexdigest()
print(hashed_str)
