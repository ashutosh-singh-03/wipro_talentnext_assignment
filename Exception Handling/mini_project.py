# Mini Project - Shopping Receipt Calculator

try:
    filename = input("Enter the file name: ")
    file = open(filename + ".txt", "r")
    lines = file.readlines()
    file.close()
    
    purchased_items = 0
    free_items = 0
    total_amount = 0
    discount = 0
    
    for line in lines:
        line = line.strip()
        
        if line == "":
            continue
        
        parts = line.split()
        
        if len(parts) == 2:
            item_name = parts[0]
            price_or_free = parts[1]
            
            if price_or_free == "Free":
                free_items = free_items + 1
            elif item_name == "Discount":
                discount = int(price_or_free)
            else:
                purchased_items = purchased_items + 1
                total_amount = total_amount + int(price_or_free)
    
    final_amount = total_amount - discount
    
    print("No of items purchased:", purchased_items)
    print("No of free items:", free_items)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found")
except ValueError:
    print("Error: Invalid data in file")
except Exception:
    print("Error: Something went wrong while processing the file")
