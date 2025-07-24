#CAFE MANAGEMENT SYSTEM
order_total = 0

while(True):
    menu = {
        "pizza":99,
        "burger":79,
        "fries":29,
        "pasta":49,
        "coffee":69,
    }
    print("-----WELCOME TO OUR PYTHON CAFE -----")
    print("1.pizza : ₹99 \n2.burger : ₹79 \n3.fries : ₹29 \n4.pasta : ₹49 \n5.coffee : ₹69")
    item_1 = input("ENTER THE NAME OF ITEM WHICH YOU WANT TO ORDER = ").lower()
    if item_1 in menu:
        order_total += menu[item_1]
        print("YOUR ITEM",item_1,"HAS BEEN ADDED TO YOUR ORDER.")
    else:
        print("THIS ITEM",item_1,"IS NOT AVAILABLE IN OUR CAFE!.\nPLEASE ORDER SOMETHING ELSE THAT WE CAN SERVE YOU.")

    another_order = input("DO YOU WANT TO ADD ANOTHER ITEM? (yes/no) = ").lower()
    if another_order == "yes":
        item_2 = input("ENTER THE NAME OF 2ND ITEM WHICH YOU WANT TO ORDER = ").lower()
        if item_2 in menu:
            order_total +=menu[item_2]
            print("ITEM",item_2,"HAS BEEN ADDED TO YOUR ORDER")
        else:
            print("THIS ITEM",item_2,"IS NOT AVAILABLE IN OUR CAFE!.\nPLEASE ORDER SOMETHING ELSE THAT WE CAN SERVE YOU.")
    
    print(f"THE TOTAL AMOUNT OF ITEMS TO PAY IS {order_total}. \nTHANKS FOR COMING HERE.")

    break