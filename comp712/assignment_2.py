from collections import defaultdict

inventory = defaultdict(int)

def add_to_inventory(invent_dict, item, quantity):
    item_quant = invent_dict[item]
    invent_dict[item] = item_quant + quantity

def show_inventory(invent_dict):
    if not invent_dict:
        print("No items found")
    else:
        for key, value in invent_dict.items():
            print(f"{key}: {value}")

def take_item_name():
    item_name = input("Enter Item name: ")
    if not item_name.isalpha():
        print("Invalid Item name")
        return None
    else:
        return item_name

def take_item_quantity():
    try:
        quantity = input("Enter Item quantity: ")
        n = int(quantity)
        return n
    except ValueError:
        print("Invalid quantity input")
        return None

add_to_inventory(inventory,"apple", 10)
add_to_inventory(inventory,"banana", 15)
add_to_inventory(inventory,"orange",8)

try:
    while True:
        print("\nWelcom to inventory management system:")
        print("1. Show all items")
        print("2. Add inventory")
        print("3. Exit")

        choice = input("Enter your option: ")

        match choice:
            case "1":
                show_inventory(inventory)
            case "2":
                item_name = take_item_name()
                while item_name is None:
                    item_name = take_item_name()
                
                quantity = take_item_quantity()
                while quantity is None:
                    quantity = take_item_quantity()
                
                add_to_inventory(inventory,item_name,quantity)
            
            case "3":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, try again.")

except KeyboardInterrupt:
    print("\nBye")
