import csv
import os

from file_managment.jsonfilemgmnt import filename


def write_csv(filename):
    data = [
        {"name" : "Sindhu", "age" : 30},
        {"name" : "telukuntla", "age":22}
    ]

    columnnames = ["name", "age"]

    with open(filename, 'w', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerows(data)

    print('CSV file written successfully')

def read_csv(filename):
    with open(filename, 'r', newline='\n') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(f'Name : {row['name']}, Age : {row['age']}')

filename = "myfile.csv"

write_csv(filename)
print('Data read from CSV file :')
read_csv(filename)