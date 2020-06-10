
items ={
    "name" : ["Milk", "Sugar", "Flour", "Coffee"],
    "quantity" : [120, 1000, 12000, 25],
    "unit" : ["l", "kg", "kg", "kg"],
    "unit_price" : [2.3, 3, 1.2, 40]
}

name = items.get("name")
quantity = items.get("quantity")
unit = items.get("unit")
unit_price = items.get("unit_price")





def get_items():
    print("Name"+'\t'+"Quantity"+'\t'+"Unit"+'\t'+"Unit Price (PLN)")
    print("----"+'\t'+"--------"+'\t'+"----"+'\t'+"----------------")
    for i in range (len(name)):
        print( str(name[i])+'\t'+ str(quantity[i])+'\t\t'+ str(unit[i]) +'\t' + str(unit_price[i]))

input("What you like to do? ")

while "add":
    print("Adding to warehouse..")
    input("Item name: ")
    input("Item quantity: ")
    input("Item unit of measure. Eg. l, kg, pcs: ")
    input("Item price in PLN: ")
    get_items()
    exit()

while "show":
    get_items()
    exit()

while "exit":
    print("Exiting... Bye!")
    exit()



