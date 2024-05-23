#!/usr/bin/env python3

import csv

def read_employees("/home/student/data/employees.csv"):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open("/home/student/data/employees.csv"), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))
