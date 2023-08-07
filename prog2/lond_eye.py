name = str(input("What is your name?"))
age = int(input("What is your age?"))
print(f"Hello {name} (age {age})")
if age < 22:
    print("You were not born when the london eye opened in 1999")
else: 
    print(f"you were {age - 23} when the london eye opened in 1999 ")