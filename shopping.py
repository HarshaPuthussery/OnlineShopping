import csv

menu = {}
menu['1']="Add Data"
menu['2']="Exit"
while True:
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])
    selection = input("Please Select : ")
    if selection=='1':
        with open('hello.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("ID\t\tProduct\t\tPrice\tQuantity")
            for row in reader:
                print(row['id'], "\t", row['Name'], "\t", row['Price'], '\t', row['Available'])
            while True:
                try:
                     Name = input("Please enter the product Name: ")
                except ValueError:
                    print("Enter valid Name :  \n")
                    continue
                else:
                    break

        with open("hello.csv", "r") as f_obj:
            check = 0
            csv_file = csv.reader(f_obj, delimiter=",")
            for line in csv_file:
                if Name in line:
                    check = 1
                    qty = int(input("Specify the quantity : "))
                    if qty <= int(line[2]):
                        print("Product is available")
                        print("Product Details \n"
                              "Product Id : ", line[0], "\n"
                                                        "Product Name : ", line[1], "\n"
                                                                                    "Product Remaining Available : ",
                              (int(line[2]) - qty), "\n"
                                                    "Product Price : ", line[3], "\n"
                                                                                 "Product Brand : ", line[5], "\n"
                                                                                                              "Qty : ",
                              qty, "\n"
                                   "Total Price : ", int(qty) * int(line[3]))
                    else:
                        print("Not enough quantity")
            if check == 0:
                print("Invalid Product Name")
    elif selection == '2':
        break
    else:
        print("Unknown Option Selected! Pleaes try again")