def takename():
    name = input("What is your name?:")
    return name

try:
    name = takename()
    if any(not(char.isalpha()) for char in name):
        raise ValueError
except ValueError:
    print("please enter a valid name")