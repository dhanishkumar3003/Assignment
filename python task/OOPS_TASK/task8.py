class shoppingCart:
    available_items={"Chicken":260,"Mutton":900,"Bread":50}
    def __init__(self):
        self.items={}
    def addItems(self):
        item=input("Enter item name: ")
        if item in shoppingCart.available_items:
            self.items[item]=shoppingCart.available_items[item]
            print("Item added successfully")
        else:
            print("item not in the list")
    def removeItems(self):
        item=input("Enter item remove: ")
        if item in self.items: 
            del self.items[item]
            print("Item removed successfully")
        else:
            print("Item not in the list")
    def totalItems(self):
        for item,price in self.items.items():
            print(item)
    def totalPrice(self):
        totalPrice=0
        for item,price in self.items.items():
            totalPrice+=price
        print(totalPrice)
s=shoppingCart()
while(True):
    print("Enter 1 to add item")
    print("Enter 2 to remove item")
    print("Enter 3 to view cart")
    print("Enter 4 to view total price")
    choice=int(input("Enter your choice"))
    if choice==1:
        s.addItems()
    elif choice==2:
        s.removeItems()
    elif choice==3:
        s.totalItems()
    elif choice==4:
        s.totalPrice()
    else:
        break