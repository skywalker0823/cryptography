#Morse.py

#This program will convert a string of text into morse code or vice versa, depending on the user's choice.

#Define the morse code dictionary
morse_code = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
}

# encode function
def encode(content):
    try:
        for letter in content:
            # Use end = ' ' to print the morse code in the same line
            if letter != ' ':
                # Search for the letter in the morse_code dictionary and print its value
                print(morse_code[letter.upper()], end = ' ')
            else:
                print(' ', end = ' ')
    except KeyError:
        print("Error input")
        exit()

# decode function
def decode(content):
    # turn morse_code into a dictionary with the values as keys and the keys as values
    morse_code_decode = {value:key for key, value in morse_code.items()}
    # Split the string into a list of words
    try:
        content = content.split(' ')
        for letter in content:
            # Search for the letter in the morse_code_decode dictionary and print its value
            if letter != '':
                print(morse_code_decode[letter], end = '')
            else:
                print(' ', end = '')
    except KeyError:
        print("Error input")
        exit()

# Main function
choice = input("Press 1 to encode, 2 to decode : ")

while True:
    if choice == "1":
        content = input("\nEnter the text to be encoded : ")
        encode(content)
    elif choice == "2":
        content = input("\nEnter the text to be decoded : ")
        decode(content)
    else:
        print("Error input")
        break
