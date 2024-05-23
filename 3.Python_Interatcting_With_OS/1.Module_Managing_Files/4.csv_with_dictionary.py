#!/usr/bin/python3
import csv

# Fetching data in the python dictionary
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"],row["users"]))
#==================================================================================

# Adding data to the dictionary
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

# First find the list of keys want to write in the file
keys = ["name","username","department"]

with open('by_department.csv','w') as by_department:
    writer = csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
