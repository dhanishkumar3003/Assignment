class Menu:
    def __init__(self, menu_card):
        self.menu_card = menu_card
    
    def display_menu(self):
        print("Menu Card:")
        for category, items in self.menu_card.items():
            print(f"{category}: {items}")

    def add_item(self):
        category = input("Enter the category: ")
        item = input("Enter the item: ")
        if category in self.menu_card:
            self.menu_card[category].append(item)
        else:
            self.menu_card[category] = [item]
        self.display_menu()

    def update_item(self):
        category = input("Enter the category: ")
        item = input("Enter the existing item: ")
        new_item = input("Enter the new item: ")

        if category in self.menu_card and item in self.menu_card[category]:
            index = self.menu_card[category].index(item)
            self.menu_card[category][index] = new_item
        else:
            print(f"{item} not found in the menu.")
        self.display_menu()

    def remove_item(self):
        category = input("Enter the category: ")
        item = input("Enter the existing item: ")
        if category in self.menu_card and item in self.menu_card[category]:
            self.menu_card[category].remove(item)
        else:
            print(f"{item} not found in the menu.")
        self.display_menu()

    def update_category(self):
        old_category = input("Enter the old category: ")
        new_category = input("Enter the new category: ")

        if old_category in self.menu_card:
            self.menu_card[new_category] = self.menu_card.pop(old_category)
        else:
            print(f"{old_category} not found in the menu.")
        self.display_menu()

    def remove_category(self):
        category = input("Enter the category to remove: ")
        if category in self.menu_card:
            self.menu_card.pop(category)
        else:
            print(f"{category} not found in the menu.")
        self.display_menu()

def main():
    menu_card = {
        'veg_starter': ['paneer 65', 'chilly paneer', 'veg crispy']
    }

    menu = Menu(menu_card)

    while True:
        print("\n1 for display menu")
        print("2 to add item to menu")
        print("3 to update item in menu")
        print("4 to remove item from menu")
        print("5 to update category in menu")
        print("6 to remove category from menu")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            menu.display_menu()
        elif choice == 2:
            menu.add_item()
        elif choice == 3:
            menu.update_item()
        elif choice == 4:
            menu.remove_item()
        elif choice == 5:
            menu.update_category()
        elif choice == 6:
            menu.remove_category()
        else:
            exit(0)

if __name__ == "__main__":
    main()
