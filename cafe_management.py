menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Coffee':80
    }
print(menu)

#greet
print("WELCOME TO PYTHON CAFE")
print("Pizza: RS. 40/-\n Pasta: RS.50/-\nBurger: RS. 60/-\nCoffee: RS. 80/- ")

order_total=0 # adds the item and also the prize of an iten, ie- order coffee will store 80/-

item_1=input("ENTER THE NAME OF ITEM YOU WANT TO ORDER")

if item_1 in menu: # if ordered item is their in list then print yes or else print no
    order_total+=menu[item_1] # if enter the item in dict, automatically prize of item will be calculated
    print(f"{item_1} has been added to your order")

else:
    print(f"sorry we are out of {item_1}")
 

another_item= input("DO YOU WANT TO ORDER SOMETHING ELSE")
if another_item=="yes":
    item_2= input("enter name of second item")
    if item_2 in menu:
     order_total+=menu[item_2]
     print(f"ITEM{item_2}HAS BEEN ADDED TO YOUR ORDER")
    else:
       print(f"ORDERED ITEM {item_2}IS NOT AVAILABLE")

    print(f"TOTAL AMOUT OF ITEMS TO PA IS {order_total}")  
    print("THANK YOU")
    