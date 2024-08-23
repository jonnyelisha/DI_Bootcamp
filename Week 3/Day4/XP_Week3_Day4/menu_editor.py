from menu_item import MenuItem
from menu_manager import MenuManager
def show_user_menu():
    while True:
        print("\nMenu:")
        print('View an Item (V)')
        print('Add an Item (A)')
        print('Delete an Item (D)')
        print('Update an Item (U)')
        print('Show the Menu (S)')
        print('Quit (Q)')
        user_choice = input("Your choise: ").upper()
        if user_choice == "V":
            view_item()
        elif user_choice == "A":
            add_item_to_menu()
        elif user_choice == 'D':
            remove_item_from_menu()
        elif user_choice == 'U':
            update_item_from_menu()
        elif user_choice == 'S':
            show_restaurant_menu()
        elif user_choice == 'Q':
            show_restaurant_menu()
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def add_item_to_menu():
    name = input("Enter the item name: ")
    price = int(input("Enter the item price: "))
    item = MenuItem(name, price)
    item.save()
    print(f"{name} was added successfully.")

def remove_item_from_menu():
    name = input("Enter the item name to remove: ")
    item = MenuItem(name, 0)
    item.delete()
    print(f"{name} was deleted successfully.")

def update_item_from_menu():
    name = input("Enter the item name to update: ")
    new_name = input("Enter the new item name: ")
    new_price = int(input("Enter the new item price: "))
    item = MenuItem(name, 0)
    item.update(new_name, new_price)
    print(f"{name} was updated to {new_name} successfully.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\nRestaurant Menu:")
    for item in items:
        print(f"{item.item_id}: {item.name_item} - {item.price_item}")

def view_item():
    name = input("Enter the item name to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Found item: {item.name_item} - {item.price_item}")
    else:
        print("Item not found.")

if __name__ == "__main__":
    show_user_menu()