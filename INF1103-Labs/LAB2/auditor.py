# auditor.py

inventory_total = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or type 'quit'): ")
    
    if user_input.lower() == "quit":
        break
        
    if not user_input.isdigit():
        print("Error: Invalid input. Please enter a valid integer.")
        failed_entries += 1
        continue
        
    stock_qty = int(user_input)
    
    if stock_qty < 0:
        print("Error: Negative numbers are not allowed.")
        failed_entries += 1
        continue
        
    inventory_total += stock_qty
    
    if inventory_total > 500:
        print("Overstock Alert: Total inventory exceeds 500 units!")
        break

print("\n--- Audit Report ---")
print(f"Total Units Processed: {inventory_total}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
