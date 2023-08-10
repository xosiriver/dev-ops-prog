import json
import csv
import sys


def csv_to_json(input_file, output_file):
    try:
        with open(input_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        print("CSV to JSON conversion successful.")
    
    except FileNotFoundError:
        print("Error: Input CSV file not found.")
    except Exception as e:
        print("An error occurred:", e)

if len(sys.argv) != 3:
    print("Usage: python csv_to_json.py <input_csv_file> <output_json_file>")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    csv_to_json(input_file, output_file)