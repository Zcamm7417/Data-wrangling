import re
from traceback import print_tb

fileName = input("Enter file name...")
with open(fileName, 'rt') as file:
    com = file.read()
com_split = com.split("-------")
com_list = com_split[3].replace('---', '').split("\n")[1:-3]
a = [x.split('(') for x in com_list]
dict_prod = {}
for i in a:
    r = dict_prod[i[0]] = i[1].replace(')', '')
for i in dict_prod.keys():
    if 'million' in dict_prod.keys():
        dict_prod[i] = float(re.findall(r'\d+\.\d+|\d+', dict_prod[i])[0]) * 1000000
    elif 'thousand' in dict_prod.keys():
        dict_prod[i] = float(re.findall(r'\d+\.\d+|\d+', dict_prod[i])[0]) * 1000
    elif 'hundred' in dict_prod.keys():
        dict_prod[i] = float(re.findall(r'\d+\.\d+|\d+', dict_prod[i])[0]) * 100

sorted_dict = {k: v for k, v in sorted(dict_prod.items(), key=lambda item: item[1], reverse=True)}
for count, product in enumerate(sorted_dict):
    count += 1
    if count <= 5:
        print(f"{count}. {product}")

# Prompt to ask for integer number to print the value in full.
keys = list(sorted_dict)
values = list(sorted_dict.values())
prompt = input("Enter integer value from 1-5...")
if prompt == "1":
    print("ACME " + keys[0] + "has " + values[0] + " units.")
elif prompt == "2":
    print("ACME " + keys[1] + "has " + values[1] + " units.")
elif prompt == "3":
    print("ACME " + keys[2] + "has " + values[2] + " units.")
elif prompt == "4":
    print("ACME " + keys[3] + "has " + values[3] + " units.")
elif prompt == "5":
    print("ACME " + keys[4] + "has " + values[4] + " units.")
else:
    print("Wrong input")
