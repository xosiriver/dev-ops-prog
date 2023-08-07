def takename():
    name = input("What is your name?:")
    return name

try:
    name = takename()
    if any(char.isalpha() for char in name) == False:
        raise ValueError
except ValueError:
    print("please enter a valid name")