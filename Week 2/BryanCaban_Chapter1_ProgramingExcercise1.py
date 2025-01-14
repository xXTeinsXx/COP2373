# Cinema Ticket preorder app
# This app will sell a total of 4=> tickets per person until the amount of 

# Checks to see if the user wan
def runcode():
    runcode = str(input("Do you want to run thid code? (y/n): "))
    return runcode.casefold()

# Prompts the user for the number of tickets they want to purchase and validates the input.
def get_tickets_purchased():
    while True:
        try:
            tickets = int(input("Enter the number of tickets you want to purchase (up to 4): "))
            if 0 < tickets <= 4:
                return tickets
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Sells tickets to the user and updates the remaining tickets and total buyers.
def sell_tickets(remaining_tickets, total_buyers):
    tickets_purchased = get_tickets_purchased()
    if tickets_purchased > remaining_tickets:
        print("Not enough tickets remaining.")
    else:
        remaining_tickets -= tickets_purchased
        total_buyers += 1
        print(f"You purchased {tickets_purchased} tickets.")
        print(f"There are {remaining_tickets} tickets remaining.")
    return remaining_tickets, total_buyers

# Main function that runs the logic of the app
def main():
    total_tickets = 20
    remaining_tickets = total_tickets
    total_buyers = 0

    while remaining_tickets > 0:
        remaining_tickets, total_buyers = sell_tickets(remaining_tickets, total_buyers)

    print(f"All tickets have been sold. There were a total of {total_buyers} buyers.")

# If the user wants to run the code main fucation will run if not it will just say it didn't run.
while runcode() == 'y':
    main()

else:
    print('Code did not run.')