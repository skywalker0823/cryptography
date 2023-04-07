import hashlib
import itertools
import string

# brute force section
hash = "d077f244def8a70e5ea758bd8352fcd8" # Replace with the MD5 hash you want to crack
chars = string.ascii_lowercase + string.digits # The characters to use in the brute-force attack
length = 5 # The max length of the input to try

for i in range(1, length + 1):
    for combination in itertools.product(chars, repeat=i):
        input_str = ''.join(combination)
        input_hash = hashlib.md5(input_str.encode()).hexdigest()
        print(input_hash)
        if input_hash == hash:
            print(f"Match found: {input_str}")
            break
    else:
        continue
    break
