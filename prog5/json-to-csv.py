import json
import csv
import sys

def json_to_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as json_file:
            data = json.load(json_file)
        
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("JSON data should be a list of dictionaries with the same keys.")
        
        keys = data[0].keys()
        
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        
        print("JSON to CSV conversion successful.")
    
    except FileNotFoundError:
        print("Error: Input JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except Exception as e:
        print("An error occurred:", e)

if len(sys.argv) != 3:
    print("Usage: python json_to_csv.py <input_json_file> <output_csv_file>")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    json_to_csv(input_file, output_file)