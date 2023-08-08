from catclass import GoodCat, BadCat, VeryBadCat, Cat_Cage

print("very bad cats need cages")

cat1 = GoodCat()
cat2 = BadCat() 
cat3 = VeryBadCat() 



@Cat_Cage
def run_in_cage():
    cat1.meow()
    cat2.meow()
    cat3.meow()

run_in_cage()