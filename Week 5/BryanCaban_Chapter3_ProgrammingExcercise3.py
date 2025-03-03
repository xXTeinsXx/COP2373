from functools import reduce

# Function to get expenses from the user
def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':  # Stop input when user types 'done'
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))  # Convert input to float
            expenses.append((expense_type, amount))  # Store expense as a tuple
        except ValueError:
            print("Invalid input. Please enter a numeric value.")  # Handle invalid input
    return expenses

# Function to analyze expenses using reduce
def analyze_expenses(expenses):
    if not expenses:
        print("No expenses to analyze.")
        return
    
    # Calculate total expense using reduce
    total = reduce(lambda acc, x: acc + x[1], expenses, 0)
    
    # Find the highest expense using reduce
    highest = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
    
    # Find the lowest expense using reduce
    lowest = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)
    
    # Display the results
    print("\nExpense Analysis:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

# Main function to run the program
def main():
    expenses = get_expenses()  # Get user expenses
    analyze_expenses(expenses)  # Analyze and display results

# Execute main function if script is run directly
if __name__ == "__main__":
    main()
