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



name.insert(0, "----")
quantity.insert(0, "--------")
unit.insert(0, "----")
unit_price.insert(0, "----------")
name.insert(0, "Name")
quantity.insert(0, "Quantity")
unit.insert(0, "Unit")
unit_price.insert(0, "Unit Price")
#print(name)

def get_items():
    #print("Name"+'\t'+"Quantity"+'\t'+"Unit"+'\t'+"Unit Price (PLN)"+'\n')
    for i in range (len(name)):
        print( str(name[i])+'\t'+ str(quantity[i])+'\t'+ str(unit.rjust(10)[i]) +'\t' + str(unit_price[i])+ '\n')

    
    



input("What you like to do?")

while "show":
    
    get_items()
    exit()



while "exit":
    print("Exiting... Bye!")
    exit()
