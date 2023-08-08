import csv 

with open("csv-heroes.csv", "r") as f:
    heroes = csv.DictReader(f)
    for hero in heroes:
        print(hero["ï»¿Name"])

