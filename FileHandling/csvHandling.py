

import csv

with open("users.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Age","City"])
    writer.writerow(["Alice",30,"New York"])
    writer.writerow(["Bob",25,"Los Angeles"])
    writer.writerow(["Charlie",35,"Chicago"])