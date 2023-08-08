class Cat:
    def __init__(self):
        pass
    
    def meow(self):
        print("MEOW")

class GoodCat(Cat):
    def __init__(self):
        pass
    
    def meow(self):
        print("PURR PURR MEOW")

class BadCat(Cat):
    def __init__(self):
        pass
    
    def meow(self):
        print("HISS")

class VeryBadCat(Cat):
    def __init__(self):
        pass
    
    def meow(self):
        raise Exception("Nope, scratch scratch")
    
def Cat_Cage(func):
        def wrapper():
            try:
                func()
            except Exception as error:
                print(f"Cat was bad: {error}, no harm was due done to Cage")
        
        return wrapper