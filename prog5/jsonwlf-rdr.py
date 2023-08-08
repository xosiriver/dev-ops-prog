import json

with open("json-wolves.json", "r") as f:
    wolves = json.load(f)

'''
for wolf in wolves:
    print(f"{wolf['name']} is owned by {wolf['Owner']}")
'''