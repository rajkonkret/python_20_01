# json
# {"name":"John", "age":30, "car":null}
import json

print_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(print_dict))  # <class 'dict'>

with open('nasze_dane.json', "w") as f:
    json.dump(print_dict, f)

# beautyfy - upiększanie
with open('nasze_dane.json', "w") as f:
    json.dump(print_dict, f, indent=4)

with open('nasze_dane.json', "r") as f:
    data = json.load(f)

print(data)
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
# <class 'dict'>