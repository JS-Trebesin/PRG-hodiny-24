import json

path = "data.json"

animal = {
    "Name": "Hugo",
    "Type": "elephant",
    "height": "tall"
}

with open(path, mode="w") as file:
    json.dump(animal, file, indent=2)


with open(path, mode="r") as file:
    data = json.load(file)

print(data)