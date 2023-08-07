import random as rd

func = lambda a, b: a + b
listmaker = lambda: sorted([rd.randint(1,1000) for i in range(1000)])
print(listmaker())