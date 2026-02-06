
# notes

# json.dump(data, file, indent=4)
# json.dump(data, file, indent=4, sort_keys=True)  
 # Sort keys alphabetically      
 # sort_keys=True
 # sort_keys=False
 



import json

data = {
    "name": "Mimoh",
    "age": 23,
    "skills": ["Python", "JS"]
}

# with open("data.json", "w") as file:

#     json.dump(data, file)


with open("data.json", "r") as file:
    data = json.load(file)
    print(data["skills"])
