
import click

@click.command()
@click.option("--fizz", default=3, help="Number to be divided for fizz")
@click.option("--buzz", default=4, help="Number to be divided for buzz")
@click.option("--count", default=20, help="Numbers to be tested for fizzbuzz")
def fizzbuzz(fizz, buzz, count):
    for i in range(count):
        if i % fizz == 0 and i % buzz == 0:
            print("fizzbuzz")
        elif i % fizz == 0:
            print("fizz")
        elif i % buzz == 0:
            print("buzz")
        else:
            print(i)
fizzbuzz()