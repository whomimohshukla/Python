

# file=open("./task.txt","w")
# file.write("This is the first line\n")
# file.write("This is the second line\n")
# file.close()

# # print(file.read())


# import csv



# with open("task.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["Name","Age","City"])
#     writer.writerow(["Alice",30,"New York"])
#     writer.writerow(["Bob",25,"Los Angeles"])
#     writer.writerow(["Charlie",35,"Chicago"])


# //read the csv file and only city

# with open("task.csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row[2])


import json

data={
  "name": "mimohshkla",
  "age":20 ,
  "skills": ["Python", "JS"]
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    data = json.load(file)
    print(data["skills"])


