import csv


#file_name = "Finance_to_work.xlsx"

#fields = []
#rows = []


Run = True

while Run:
    print("Welcome to the finance tracker!")
    print("All data entered are going to be run on the notebooks cells where we will be looking into the data")
    print("And the Graphs will be all diplayed here")

    choice = input("Do you want to keep running the program?:  ")
    match choice:
        case "y":
            Run = False

        case _: Run = True

