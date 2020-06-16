import csv

items ={
    "name" : ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity" : [120, 1000, 12000, 25],
    "unit" : ["l", "kg", "kg", "kg"],
    "unit_price" : [2.3, 3, 1.2, 40]
}

sold_items = {
    "name" : [],
    "quantity" : [],
    "unit" : [],
    "unit_price" : []
}

acceptable_units = ["l", "kg", "pcs"]
name = items.get("name")
quantity = items.get("quantity")
unit = items.get("unit")
unit_price = items.get("unit_price")

costs = 0
income = 0
sold_name = []
sold_items["name"].append(sold_name)
sold_quantity = []
sold_items["quantity"].append(sold_quantity)
sold_items["unit"].append(unit)
sold_items["unit_price"].append(unit_price)

def get_items():
    print("Name"+'\t'+"Quantity"+'\t'+"Unit"+'\t'+"Unit Price (PLN)")
    print("----"+'\t'+"--------"+'\t'+"----"+'\t'+"----------------")
    for i in range (len(name)):
        print( str(name[i])+'\t'+ str(quantity[i])+'\t\t'+ str(unit[i]) +'\t' + str(unit_price[i]))
    main()

def add_item():
    print("Adding to warehouse..")
    name.append(input("Item name: "))
    while True:
        try:
            quantity.append(float(input("Item quantity: ")))
            break
        except ValueError:
            print("Incorrect value! Try again.")
            continue
    while True:
        try:
            text = input("Item unit of measure e.g. l, kg, pcs: ")
            text = text.lower()
            if text in acceptable_units:
                unit.append(text)
                break
            else:
                print("Incorrect value! Try again.")
                continue
        except ValueError:
            pass
    while True:
        try:
            unit_price.append(float(input("Item price in PLN: ")))
            break
        except ValueError:
            print("Incorrect value! Try again.")
            continue        
 
    get_items()

def sell_item():
    while True:
        try:
            item_to_sell = input("Item name: ")
            if item_to_sell in name:
                sale_index = name.index(item_to_sell)
                sold_name.append(item_to_sell)
                quantity_to_sell = float(input("Quantity to sell: "))
                quantity_before_sell = float(quantity[sale_index])
                quantity[sale_index] = quantity_before_sell - quantity_to_sell
                sold_quantity.append(quantity_to_sell)
                print(f"Successfully sold {quantity_to_sell} {unit[sale_index]} of {item_to_sell}")
                get_items()
            else:
                print("Product not in list! Try again!")
                add_question = input("Would you like add product to list? [Y/N] ")
                if add_question == "Y":
                    add_item()
                elif add_question == "N":
                    main()
                else:
                    print("Wrong answer! Try again!")
                    main()
                    
        except ValueError:
            pass

def get_costs():
    global costs
    for i in range (len(name)):
        costs += quantity[i] * unit_price[i]

    print(f"Costs: {costs}")

def get_income():
    global income
    for i in range (len(sold_name)):
        income += sold_quantity[i] * unit_price[i]
        

    print(f"Income: {round(income, 2)}")

def get_revenue():
    revenue = (income - costs)
    print(f"-------- \nRevenue: {round(revenue, 2)} PLN")

def export_items_to_csv():
    with open('magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'name': 'Milk', 'quantity': '120', 'unit': 'l', 'unit_price': '2.3'})
        writer.writerow({'name': 'Sugar', 'quantity': '1000', 'unit': 'kg', 'unit_price': '3'})
        writer.writerow({'name': 'Flour', 'quantity': '12000', 'unit': 'kg', 'unit_price': '1.2'})
        writer.writerow({'name': 'Coffee', 'quantity': '25', 'unit': 'kg', 'unit_price': '40'})
        print("Successfully exported to magazyn.csv")


def main():
    menu = input("What you like to do? ")

    if menu == "add":
        add_item()
        exit()

    elif menu =="show":
        get_items()
        exit()

    elif menu == "exit":
        print("Exiting... Bye!")
        exit()

    elif menu == 'sale':
        sell_item()
        exit()

    elif menu == 'costs':
        get_costs()
        exit()
    
    elif menu == 'show_revenue':
        print("Revenue breakdown (PLN)")
        get_income()
        get_costs()
        get_revenue()
        main()
    
    elif menu == 'save':
        export_items_to_csv()
        main()

    else:
        main()



if __name__ == "__main__":
    main()
    




