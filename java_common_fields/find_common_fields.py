import json
import os

# author: roi
def open_file(class_name, root_path):
    file_name = class_name + ".java"
    for root, dirs, files in os.walk(root_path):
        if file_name in files:
            return open(os.path.join(root, file_name), encoding='utf-8')


def get_fields(file):
    field_list = []
    for line in file:
        line = line.strip()
        if line.endswith(';') and line.startswith("private") and 'final' not in line:
            field_list.append(line.split(" ")[2].replace(';', ''))
    return field_list


class_a = input("Name of class A: ")
class_b = input("Name of class B: ")

print('=====================================================================')

root_path = json.load(open("config.json"))['root_path']

file_a = open_file(class_a, root_path)
file_b = open_file(class_b, root_path)

fields_a = get_fields(file_a)
fields_b = get_fields(file_b)

total = 0
for field in fields_a:
    if field in fields_b:
        print(field)
        total += 1
print('---------------------------------------------------------------------')
print('Total:', total)
print('=====================================================================')
input('Done. Press enter to exit. ') # remove this line if you're calling this script from cli
