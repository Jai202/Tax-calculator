# tax calculator for multiple items
def calcTax(items, tax=0.13):

    # declare total
    tC = 0

    # calculate total
    for i in range(0, len(items)):
        tC += items[i]
    
    return tC * (1 + float(tax))



#MAIN

# intro text
print("Hello, and welcome to Jai's price calculator!\nThis program allows you to calculate tax on essential or personal needs!\n\n")

# get need
needs = raw_input("Is your item a 'essential' need or a 'personal' need? ")

# get items
itemN = int(raw_input("Enter the number of items you will be purchasing: "))
items = [float(raw_input("ITEM " + str(i) + ": $")) for i in range(1, itemN+1)]

# calculate tax
if needs == "essential":

    print("\nTotal cost: $" + str(calcTax(items, 0)))

else:

    print("\nTotal cost: $" + str(calcTax(items)))
raw_input()