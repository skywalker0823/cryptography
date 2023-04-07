# accept input from the user, to encode or decode URI

import urllib.parse


while True:
    choice = input("\nInsert A/a to encode, B/b to decode, Q/q to quit: \n")
    try:
        if choice == "A" or choice == "a":
            content = input("\nInsert the text to encode: \n")
            result = urllib.parse.quote(content)
            print("result---> "+result+"\n")
        elif choice == "B" or choice == "b":
            content = input("\nInsert the text to encode: \n")
            result = urllib.parse.unquote(content)
            print("result---> "+result+"\n")
        elif choice == "Q" or choice == "q" or choice == "exit":
            break
        else:
            print("Error input")
            pass
    except ValueError:
        print("Error input")
        exit()