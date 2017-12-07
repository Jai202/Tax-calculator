 #INTRODUCTION
print("Hello, and welcome to Jai's price calculator! This program allows you to calculate tax on essential or personal needs!")
print ("")



#INPUT
needs= input("Is your item a essential need or a personal need? ")
if needs== "essential":
   #OUTPUT
   print("You won't be charged tax for this item")
   #INPUT
   items= int(input("How many items would you like to purchase? (Max 3) "))
   if items==1:
       #OUTPUT
       print("The price is going to be the same")
   elif items==2:
        #INPUT
        priceone= float(input("Please enter the price of the first item you maybe interested in purchasing! "))
        pricetwo= float(input("Please enter the price of the second item you maybe interested in purchasing! "))
        #CALCULATION
        cost= priceone+pricetwo + pricethree
        #OUTPUT
        print("Your cost will be", cost)
   else:
        #INPUT
        priceone= float(input("Please enter the price of the first item you maybe interested in purchasing! "))
        pricetwo= float(input("Please enter the price of the second item you maybe interested in purchasing! "))
        pricethree = float(input("Please enter the price of the third item you maybe interested in purchasing! "))
        #CALCULATION
        cost=priceone+pricetwo+pricethree
        print("Your cost will be",cost)
else:
    #OUTPUT
    print("Sorry, you will have to pay tax for this item! ")
    items= int(input("How many items would you like to purchase? (Max 3) "))
    if items==1:
        #INPUT
        priceone= float(input("Please enter the price of the first item you maybe interested in purchasing! "))
        #CALUCLATION
        total = priceone * 1.13
        print("Your cost will be", total)
    elif items==2:
        #INPUT
        priceone= float(input("Please enter the price of the first item you maybe interested in purchasing! "))
        pricetwo= float(input("Please enter the price of the second item you maybe interested in purchasing! "))
        pricethree = float(input("Please enter the price of the third item you maybe interested in purchasing! "))
        cost= priceone+pricetwo + pricethree
        #CALCULATION
        total = cost * 1.13
        #OUTPUT
        print("Your cost will be", total)
    else:
        #INPUT
        priceone= float(input("Please enter the price of the first item you maybe interested in purchasing! "))
        pricetwo= float(input("Please enter the price of the second item you maybe interested in purchasing! "))
        pricethree = float(input("Please enter the price of the third item you maybe interested in purchasing! "))
        cost= priceone+pricetwo + pricethree
        #CALCULATION
        total = cost * 1.13
        #OUTPUT
        print("Your cost will be", total)


