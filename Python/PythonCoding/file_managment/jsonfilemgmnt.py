import json
import os
from textwrap import indent


def write_json(filename):
    data = {
        "people":[
            {"name" : "John Doe", "age": 30},
            {"name" : "Jane Smith", "age" : 25}
        ]
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f'Wrote {filename} successfully')

def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        for person in data["people"]:
            print(f'Name: {person['name']}, Age: {person['age']}')

filename = "myfile.json"

write_json(filename)
print('Data read from CSV file : ')
read_json(filename)