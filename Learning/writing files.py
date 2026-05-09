#Python writing files (.txt, .json, .csv)

#txt_data = "i like pizza"
#
#file_path = "D:/OneDrive/Desktop/test.txt"
#
#with open(file_path, "a") as file:
#    file.write("\n " + txt_data)
#    print(f"txt file '{file_path}' was created")



#import json
#
#employee ={
#        "name": "spongebob",
#        "age" : 30,
#        "job": "cook"
#}

#file_path = "D:/OneDrive/Desktop/test.json"
#
#try:
#    with open(file_path,"w") as file:
#        json.dump(employee,file, indent = 4)
#        print(f"json file '{file_path}' was created ")
#except FileExistsError:
#    print("That file already exists")



import csv
employee =[["name", "age","job"],
           ["spongebob", 30, "cook"],
           ["Patrick",35,"Unemployed"],
           ["Sandy",27,"Scientist"]]


file_path = "D:/OneDrive/Desktop/test.csv"

try:
    with open(file_path,"w", newline="") as file:
       writer = csv.writer(file)
       for row in employee:
           writer.writerow(row)
    print(f"csv file '{file_path}' was created ")
except FileExistsError:
    print("That file already exists")