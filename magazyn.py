
items ={
    "name" : ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity" : [120, 1000, 12000, 25],
    "unit" : ["l", "kg", "kg", "kg"],
    "unit_price" : [2.3, 3, 1.2, 40]
}
acceptable_units = ["l", "kg", "pcs"]
name = items.get("name")
quantity = items.get("quantity")
unit = items.get("unit")
unit_price = items.get("unit_price")

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
                quantity_to_sell = float(input("Quantity to sell: "))
                quantity_before_sell = float(quantity[sale_index])
                quantity[sale_index] = quantity_before_sell - quantity_to_sell
                get_items()
            else:
                print("Product not in list! Try again!")
                add_question = input("Would you like add product to list? [Y/N] ")
                while add_question == "Y":
                    add_item()
                while add_question == "N":
                    main()
                    
        except ValueError:
            pass

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

    else:
        main()



if __name__ == "__main__":
    main()
    




