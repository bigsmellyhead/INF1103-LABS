# modular_auditor.py

def get_valid_input():
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

    return stock_qty

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("\n--- Audit Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    
def main():
    inventory_total = 0
    failed_entries = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        elif result is None:
            failed_entries += 1
            continue

        delivery_amount = result

        inventory_total = process_delivery(inventory_total, delivery_amount)

        # Commented out // Unsure if 500 stock limit still applies for this Lab?
        # if inventory_total > 500:
            # print("Overstock Alert: Total inventory exceeds 500 units!")
            # break

        tax = calculate_tax(delivery_amount)
        print(f"Delivery processed successfully. Tax for this delivery: {tax:.2f}")

    generate_report(inventory_total, failed_entries)

if __name__ == "__main__":
    main()
