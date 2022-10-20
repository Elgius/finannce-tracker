import csv


file_name = "for data work.csv"

fields = []
rows = []

with open(file_name,"r") as file:
    data = csv.reader(file)

    fields = next(data)

    for row in data:
        rows.append(row)


print("here is the csv file for inspection: ")
print('Field names are as follows: ' + ',' .join(field for field in fields ))

for row in rows[:5]:
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')

#
#Run = True
#
#while Run:
#    print("Welcome to the finance tracker!")
#    print("All data entered are going to be run on the notebooks cells where we will be looking into the data")
#    print("And the Graphs will be all diplayed here")
#
#    data_bank = {
#
#
#    }
#
#    choice = input("Do you want to keep running the program?:  ")
#    match choice:
#        case "y":
#            Run = False
#
#        case _: Run = True
#
#