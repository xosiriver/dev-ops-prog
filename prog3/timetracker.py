import time
import random as rd

def timetrack(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        print(f"Function took {time.time() - before} seconds")
        return val
    return wrapper


listmaker = lambda: sorted([rd.randint(1,1000) for i in range(1000)])
listmaker = timetrack(listmaker)
print(listmaker())