# FIXED CODE Debugging Exercise
# This code is the fixed and improved version of the broken code

def check_number(number, name):
    # Makes sure a number is valid
    try:
        num = float(number)
        if num < 0:
            raise ValueError(f"{name} can't be negative!")
        return num
    except:
        raise ValueError(f"Hey, {name} needs to be a real number!")

def calculate_discount(price, discount_rate):
    # Figures out how much discount to give
    price = check_number(price, "price")
    discount_rate = check_number(discount_rate, "discount rate")
    
    if discount_rate > 1:
        raise ValueError("Discount rate should be less than 1 (like 0.2 for 20%)")
        
    return round(price * discount_rate, 2)

def apply_discount(price, discount_amount):
    # Takes off the discount from the price
    price = check_number(price, "price")
    discount_amount = check_number(discount_amount, "discount amount")
    
    return round(price - discount_amount, 2)

def main():
    # List of products and their discounts
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": 500, "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    # Go through each product and calculate its discount
    for product in products:
        try:
            price = product["price"]
            discount_rate = product["discount_rate"]
            
            print(f"\nCalculating discount for: {product['name']}")
            discount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount)

            print(f"Original Price: ${price}")
            print(f"You save: ${discount}")
            print(f"Final Price: ${final_price}")
            
        except ValueError as e:
            print(f"\nOops! Problem with {product['name']}: {str(e)}")
        except:
            print(f"\nSomething went wrong with {product['name']}!")

if __name__ == "__main__":
    main()