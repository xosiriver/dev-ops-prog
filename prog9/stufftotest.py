import random, string

def exceg():
    raise ValueError

def change(x):
    x = "".join(random.choice(string.ascii_lowercase) for i in range(5))