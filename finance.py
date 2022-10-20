import csv

Run = True

while Run:
    print("Welcome to the finance tracker!")
    print("All data entered are going to be run on the notebooks cells where we will be looking into the data")
    print("And the Graphs will be all diplayed here")

    Spending = input("What did you spend on?:  ")
    Quantity = input("How many times did you buy it?:   ")
    Money = input("How much did this cost?:   ")

    fields = ["Name", "Quantity", "Cost($)"]
    #fields = ['Name', 'Branch', 'Year']
    row = [[Spending, Quantity, Money]]

    with open("for data work.csv" , "w") as file:
        pen = csv.writer(file)
        pen.writerow(fields)
        pen.writerows(row)


    with open("for data work.csv","r") as file:
        data = csv.reader(file)
        for lines in file:
            print(lines)




    choice = input("Do you want to end the program?: [y/n] ")
    answer = choice.lower()
    match answer:
        case "y":
            Run = False

        case "n":
            Run = True

        case _: print("Please type y or n")


#last update on 20-10-2022