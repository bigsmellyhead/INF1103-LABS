# modular_auditor.py
import os

def load_inventory():
    total = 0
    history = []
    
    if os.path.exists("inventory.txt"):
        try:
            with open("inventory.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    total = int(lines[0].strip())
                    
                    for line in lines[1:]:
                        val = line.strip()
                        if val: 
                            history.append(val)

        except (IOError, ValueError):
            print("Error reading inventory file. Starting with empty inventory.")
            total = 0
            history = []
            
    return total, history

def save_inventory(total, history):
    try:
        with open("inventory.txt", "w") as file:
            file.write(f"{total}\n")
            for item in history:
                file.write(f"{item}\n")
    except IOError as e:
        print(f"Error saving file: {e}")

def get_valid_input():
    product_name = input("Enter Product Name: ").strip()
    if product_name.lower() == "quit":
        return "quit", None
            
    if not product_name:
        print("Error: Product name cannot be empty.")
        return None, None

    if not any(char.isalpha() for char in product_name):
        print("Error: Product name must contain at least some letters (e.g., cannot be just numbers).")
        return None, None
    
    user_input = input("Enter stock quantity (or type 'quit'): ")

    if user_input.lower() == "quit":
        return "quit"
        
    try:
        stock_qty = int(user_input)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None
    
    if stock_qty < 0:
        print("Error: Negative numbers are not allowed.")
        return None

    return product_name, stock_qty

def process_delivery(current_total, new_value):
    return current_total + new_value

# def calculate_tax(amount):
    #return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("\n--- Audit Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    
def main():
    inventory_total, transaction_history = load_inventory()
    failed_entries = 0

    print("Current Orders:\n")
    if transaction_history:
        for order in transaction_history:
            print(order)
    else:
        print("(No previous orders found)")
    print()

    next_id = 1001 + len(transaction_history)

    print(f"Loaded previous inventory total: {inventory_total}")

    while True:
        product_name, quantity = get_valid_input()
        
        if product_name == "quit":
            save_inventory(inventory_total, transaction_history)
            print("Order successfully saved to inventory.txt")
            break
            
        if product_name is None or quantity is None:
            failed_entries += 1
            print()
            continue
            
        inventory_total = process_delivery(inventory_total, quantity)
        
        order_record = f"{next_id}, {product_name}, {quantity}"
        transaction_history.append(order_record)
        
        print(f"\nNew Order Added:")
        print(order_record)
        print()
        
        next_id += 1

    generate_report(inventory_total, failed_entries)

if __name__ == "__main__":
    main()
