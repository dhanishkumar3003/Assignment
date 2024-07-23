veg_starter = ['panner 65', 'chilly powder', 'veg crispy']

def display_menu():
    print(veg_starter)

def add_starter():
    veg_starter.append(input("Enter item name: "))

def update_starter():
    name = input("Enter item name to update: ")
    if name in veg_starter:
        pos = veg_starter.index(name)
        veg_starter[pos] = input("Enter new item name: ")
    else:
        print("Item not found in the menu.")

def remove_starter():
    item_to_remove = input("Enter item name to remove: ")
    if item_to_remove in veg_starter:
        veg_starter.remove(item_to_remove)
    else:
        print("Item not found in the menu.")

def menu(choice):
    if choice == 1:
        display_menu()
    elif choice == 2:
        add_starter()
    elif choice == 3:
        update_starter()
    elif choice == 4:
        remove_starter()
    else:
        exit(0)

def main():
    while True:
        print("\n1 for display menu")
        print("2 to add starter menu")
        print("3 to update starter menu")
        print("4 to remove starter menu")
        choice = int(input("Enter your choice: "))
        menu(choice)

if __name__ == "__main__":
    main()
