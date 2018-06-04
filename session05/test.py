#dictionary
#Create
person = {
    #key: value
    "name": "Quý",
    "age": 20,
    "ex": 0,
    "favs": ["Manga", "Coding"]
}

# print(person)
# name = person["name"]
# print(name)


#Update
# person["length"] = 20
# print(person)
# person["length"] = 10
# print(person)

#Delete
# del person["length"]
# key = "length"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

# for k in person:
#     print(k, person[k])

for v in person.values():
    print(v)
# for k, v in person.items():
#     print(k, v)