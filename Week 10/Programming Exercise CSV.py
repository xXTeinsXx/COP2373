import csv

def create_grades_file():
    
    # Creates a CSV file containing student information and exam grades.
    # Allows instructor to input number of students and their details.
    
    try:
        # Get number of students from the instructor
        num_students = int(input("Enter the number of students: "))
        
        # Open the CSV file for writing
        with open('grades.csv', 'w', newline='') as csvfile:
            # Create a CSV writer with the specified header
            fieldnames = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header row
            writer.writeheader()
            
            # Get information for each student
            for i in range(num_students):
                print(f"\nEnter information for student {i+1}:")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                
                # Get exam grades, ensuring they are integers
                exam1 = int(input("Exam 1 Grade: "))
                exam2 = int(input("Exam 2 Grade: "))
                exam3 = int(input("Exam 3 Grade: "))
                
                # Write the student record to the CSV file
                writer.writerow({
                    'First Name': first_name,
                    'Last Name': last_name,
                    'Exam 1': exam1,
                    'Exam 2': exam2,
                    'Exam 3': exam3
                })
        
        print(f"\nSuccessfully created grades.csv with {num_students} student records.")
    
    except ValueError:
        print("Error: Please enter a valid number for the student count or exam grades.")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_grades_file():
    
    # Reads the grades.csv file and displays the data in a formatted table.
    # Uses the with keyword to ensure proper file handling.

    try:
        # Open the CSV file for reading
        with open('grades.csv', 'r', newline='') as csvfile:
            # Create a CSV reader
            reader = csv.DictReader(csvfile)
            
            # Get the fieldnames from the reader
            fieldnames = reader.fieldnames
            
            # Print the header
            print("\nStudent Grades Report")
            print("-" * 70)
            
            # Format and print the column headers
            header_format = "{:<15} {:<15} {:>10} {:>10} {:>10}"
            print(header_format.format(*fieldnames))
            print("-" * 70)
            
            # Format and print each row of data
            row_format = "{:<15} {:<15} {:>10} {:>10} {:>10}"
            for row in reader:
                print(row_format.format(
                    row['First Name'],
                    row['Last Name'],
                    row['Exam 1'],
                    row['Exam 2'],
                    row['Exam 3']
                ))
            
            print("-" * 70)
    
    except FileNotFoundError:
        print("Error: grades.csv file not found. Please run the create_grades_file function first.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():

    # Main function to provide a menu for the user to choose between creating
    # a new grades file or displaying an existing one.

    while True:
        print("\nStudent Grades Management System")
        print("1. Create new grades.csv file")
        print("2. Display existing grades.csv file")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            create_grades_file()
        elif choice == '2':
            display_grades_file()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
