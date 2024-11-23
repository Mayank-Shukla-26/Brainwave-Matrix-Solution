import json

DATA_FILE = "electronics_store_inventory.json"

# Load existing data or create a new file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_item(inventory):
    item_id = input("Enter Item ID: ")
    if item_id in inventory:
        print("Item ID already exists! Try updating the item instead.")
        return
    
    details = {}
    details["name"] = input("Enter Product Name (e.g., iPhone 14): ")
    details["category"] = input("Enter Product Category (e.g., Smartphone, Laptop, TV): ")
    details["brand"] = input("Enter Brand (e.g., Apple, Samsung, Sony): ")
    details["model"] = input("Enter Model (e.g., A2891, Galaxy S23): ")
    details["price"] = float(input("Enter Price (in INR): "))
    details["quantity"] = int(input("Enter Quantity in Stock: "))
    details["warranty"] = input("Enter Warranty Period (e.g., 1 year, 2 years): ")
    
    # Allow additional specifications
    add_specs = input("Do you want to add specifications (e.g., RAM, Storage)? (yes/no): ").strip().lower()
    if add_specs == "yes":
        details["specifications"] = {}
        while True:
            spec_key = input("Enter Specification Name (e.g., RAM, Storage): ")
            spec_value = input(f"Enter Value for {spec_key} (e.g., 8GB, 256GB): ")
            details["specifications"][spec_key] = spec_value
            more_specs = input("Add another specification? (yes/no): ").strip().lower()
            if more_specs != "yes":
                break
    
    inventory[item_id] = details
    print("Product added successfully!")

def view_inventory(inventory):
    print("\nCurrent Inventory:")
    if not inventory:
        print("No products in the inventory.")
        return

    for item_id, details in inventory.items():
        print(f"\nID: {item_id}")
        print(f"  Name: {details['name']}")
        print(f"  Category: {details['category']}")
        print(f"  Brand: {details['brand']}")
        print(f"  Model: {details['model']}")
        print(f"  Price: ₹{details['price']}")
        print(f"  Quantity: {details['quantity']}")
        print(f"  Warranty: {details['warranty']}")
        
        if "specifications" in details:
            print("  Specifications:")
            for spec, value in details["specifications"].items():
                print(f"    {spec.capitalize()}: {value}")

def update_item(inventory):
    item_id = input("Enter Product ID to update: ")
    if item_id in inventory:
        print(f"Current details for ID {item_id}:")
        for key, value in inventory[item_id].items():
            if isinstance(value, dict):  # For specifications
                print(f"  {key.capitalize()}:")
                for sub_key, sub_value in value.items():
                    print(f"    {sub_key.capitalize()}: {sub_value}")
            else:
                print(f"  {key.capitalize()}: {value}")
        
        update_field = input("Enter the field you want to update (e.g., quantity, price, specifications): ").strip().lower()
        if update_field in inventory[item_id]:
            if update_field == "quantity":
                new_value = int(input("Enter new Quantity: "))
                inventory[item_id][update_field] = new_value
            elif update_field == "price":
                new_value = float(input("Enter new Price: "))
                inventory[item_id][update_field] = new_value
            elif update_field == "specifications":
                print("Updating specifications. Current specifications:")
                for spec, value in inventory[item_id][update_field].items():
                    print(f"  {spec.capitalize()}: {value}")
                spec_key = input("Enter the specification to update or add (e.g., RAM): ")
                spec_value = input(f"Enter the new value for {spec_key}: ")
                inventory[item_id][update_field][spec_key] = spec_value
            else:
                new_value = input(f"Enter new value for {update_field}: ")
                inventory[item_id][update_field] = new_value
            print("Product updated successfully!")
        else:
            print(f"Field '{update_field}' not found in the product.")
    else:
        print("Product not found!")

def delete_item(inventory):
    item_id = input("Enter Product ID to delete: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Product deleted successfully!")
    else:
        print("Product not found!")

def main():
    inventory = load_data()
    while True:
        print("\nElectronics Store Inventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            delete_item(inventory)
        elif choice == "5":
            save_data(inventory)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
