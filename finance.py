import csv

Run = True

while Run:
    print("Welcome to the finance tracker!")
    print("All data entered are going to be run on the notebooks cells where we will be looking into the data")
    print("And the Graphs will be all diplayed here")

    data_bank = {}

    with open("for data work.csv","r") as file:
        data = csv.reader(file)

        for lines in file:
            print(lines)




    choice = input("Do you want to keep running the program?: [y/n] ")
    choice = choice.lowercase()
    match choice:
        case "y":
            Run = False

        case "n":
            Run = True

        case _: print("Please type y or n")


#last update on 20-10-2022