import sys
from art import *

text = str(sys.argv[1])


with open("new_file.txt", "w") as file:
    for _ in range(10):
        file.write(text2art(text, font="random"))
