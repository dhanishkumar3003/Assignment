menu_card = {
    'veg_starter': ['paneer 65', 'chilly paneer', 'veg crispy']
}

def display_menu():
    print("Menu Card:")
    for category, items in menu_card.items():
        print(f"{category}: {items}")

def add_item():
    category=input("Enter the category : ")
    item=input("Enter the item : ")
    if category in menu_card:
        menu_card[category].append(item)
    else:
        menu_card[category]=[]
        menu_card[category].append(item)
    display_menu()

def update_item():
    category=input("Enter the category : ")
    item=input("Enter the exisiting item : ")
    new_item=input("Enter the new item : ")
    
    if item in menu_card[category]:
        index = menu_card[category].index(item)
        menu_card[category][index] = new_item
    else:
        print(f"{item} not found in the menu.")
    display_menu()

def remove_item():
    category=input("Enter the category : ")
    item=input("Enter the exisiting item : ")
    if item in menu_card[category]:
        menu_card[category].remove(item)
    else:
        print(f"{item} not found in the menu.")
    display_menu()

def update_category():
    old_category = input("Enter the old category: ")
    new_category = input("Enter the new category: ")
    
    if old_category in menu_card:
        menu_card[new_category] = menu_card.pop(old_category)
    else:
        print(f"{old_category} not found in the menu.")
    display_menu()
def remove_category():
    category= input("Enter the category to remove: ")
    menu_card.pop(category)
    display_menu()
def main():
    
    while(True):
        print("\n1 for display menu")
        print("2 to add item menu")
        print("3 to update item menu")
        print("4 to remove item menu")
        print("5 to update category in menu")
        print("6 to remove category in menu")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            display_menu()
        elif choice == 2:
            add_item()
        elif choice == 3:
            update_item()
        elif choice == 4:
            remove_item()
        elif choice == 5:
            update_category()
        elif choice == 6:
            remove_category()
        else:
            exit(0)

if __name__=="__main__":
    main()