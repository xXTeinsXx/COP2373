"""
Student Grade Analysis Program
------------------------------
Author: Bryan Caban
Assignment: Chapter 12 Programming Exercise 12

Overview:
This program analyzes student grade data stored in a CSV file using NumPy for numerical operations.
It provides statistical insights into student performance by calculating various metrics for each exam
and for the overall dataset.

Things the  program does:
- Loads student grade data from a CSV file
- Calculates mean, median, standard deviation, minimum, and maximum for each exam
- Determines pass/fail statistics for each exam (passing grade is 60 or above)
- Calculates overall statistics across all exams
- Provides user-friendly interface for file selection and program execution
"""

# Import necessary libraries
import numpy as np  # For numerical operations and array manipulation
import csv  # For reading CSV files
import os  # For file path operations

def load_data(filename):
    """
    Load student grade data from a CSV file into a numpy array
    
    Parameters:
    filename (str): Path to the CSV file
    
    Returns:
    tuple: (headers, data) where headers are column names and data is a numpy array of grades
    """
    # Check if file exists before attempting to open it
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None, None
    
    # Initialize empty lists to store the data
    headers = []
    data = []
    
    try:
        # Open and read the CSV file
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            # Get headers from first row of the CSV file
            headers = next(csv_reader)
            
            # Read data rows from the CSV file
            for row in csv_reader:
                # Convert string values to float for grades
                # Assuming first column is student ID or name and rest are grades
                numeric_row = [row[0]] + [float(val) for val in row[1:]]
                data.append(numeric_row)
        
        # Check if any data was loaded (empty file check)
        if not data:
            print("Error: No data found in the file or file is empty.")
            return None, None
            
        # Convert data to numpy array, excluding the first column (names/IDs)
        # This creates a 2D array where each row is a student and each column is an exam
        grades_array = np.array([row[1:] for row in data])
        
        return headers, grades_array
    
    # Handle any exceptions that might occur during file reading
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def analyze_grades(headers, grades_array):
    """
    Perform statistical analysis on grade data
    
    Parameters:
    headers (list): Column headers from CSV file
    grades_array (numpy.ndarray): Array of student grades
    """
    # Print first few rows to understand the data structure
    print("\n=== First 3 rows of data ===")
    print(f"Headers: {headers}")
    # Print first 3 rows or all rows if less than 3
    print(grades_array[:3] if len(grades_array) >= 3 else grades_array)
    
    # Calculate statistics for each exam (column)
    print("\n=== Statistics for each exam ===")
    # Exclude first column (student ID/name) from headers
    exam_headers = headers[1:]
    
    # Loop through each exam column
    for i, exam_name in enumerate(exam_headers):
        # Extract grades for the current exam
        exam_grades = grades_array[:, i]
        
        # Print statistics for this exam
        print(f"\nExam: {exam_name}")
        print(f"Mean: {np.mean(exam_grades):.2f}")          # Average grade
        print(f"Median: {np.median(exam_grades):.2f}")       # Middle value when sorted
        print(f"Standard Deviation: {np.std(exam_grades):.2f}")  # Measure of spread
        print(f"Minimum: {np.min(exam_grades):.2f}")         # Lowest grade
        print(f"Maximum: {np.max(exam_grades):.2f}")         # Highest grade
        
        # Pass/fail analysis for this exam (passing grade is 60 or above)
        passing_mask = exam_grades >= 60  # Boolean mask of passing grades
        passed = np.sum(passing_mask)     # Count of True values (passing grades)
        failed = len(exam_grades) - passed  # Count of failing grades
        
        # Calculate and print passing/failing percentages
        print(f"Passed: {passed} students ({passed/len(exam_grades)*100:.2f}%)")
        print(f"Failed: {failed} students ({failed/len(exam_grades)*100:.2f}%)")
    
    # Calculate overall statistics (all exams combined)
    print("\n=== Overall Statistics (all exams) ===")
    # Flatten the 2D array to treat all grades equally
    all_grades = grades_array.flatten()
    
    # Print overall statistics
    print(f"Overall Mean: {np.mean(all_grades):.2f}")        # Average of all grades
    print(f"Overall Median: {np.median(all_grades):.2f}")     # Middle value of all grades
    print(f"Overall Standard Deviation: {np.std(all_grades):.2f}")  # Spread of all grades
    print(f"Overall Minimum: {np.min(all_grades):.2f}")       # Lowest grade overall
    print(f"Overall Maximum: {np.max(all_grades):.2f}")       # Highest grade overall
    
    # Overall pass percentage calculation
    passing_grades = np.sum(all_grades >= 60)  # Count grades >= 60
    total_grades = all_grades.size             # Total number of grades
    pass_percentage = (passing_grades / total_grades) * 100  # Calculate percentage
    
    # Print passing statistics
    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")
    print(f"Total Passing Grades: {passing_grades} out of {total_grades}")

def get_file_path():
    """
    Get the file path from the user or use a default path
    
    Returns:
    str: Path to the CSV file
    """
    # Define default path for convenience
    default_path = "student_grades.csv"
    
    # Prompt user for file path or use default
    file_path = input(f"Enter the path to the CSV file (or press Enter to use '{default_path}'): ")
    
    # If user didn't enter anything, use the default path
    if not file_path:
        file_path = default_path
        
    return file_path

def runcode():
    """
    Ask the user if they want to run the code
    
    Returns:
    bool: True if user wants to run the code, False otherwise
    """
    # Ask user if they want to run the program
    response = input("Do you want to run this code? (y/n): ")
    
    # Convert response to lowercase and check if it's 'y'
    return response.lower() == 'y'

def main():
    """
    Main function to run the program
    """
    # Get file path from user
    file_path = get_file_path()
    
    # Inform user about file loading
    print(f"Loading student grade data from: {file_path}")
    
    # Load data from the CSV file
    headers, grades_array = load_data(file_path)
    
    # Check if data was loaded successfully
    if headers is not None and grades_array is not None:
        # Print success message with student count
        print(f"Successfully loaded data for {len(grades_array)} students.")
        
        # Analyze the grade data
        analyze_grades(headers, grades_array)
    else:
        # Print error message if data loading failed
        print("Failed to load data. Please check the file path and format.")

# Entry point of the program
if __name__ == "__main__":
    # Main program loop
    while True:
        # Check if user wants to run the program
        if runcode():
            # Run the main function
            main()
        else:
            # Exit message when user chooses to quit
            print('Goodbye! 👋 See you next time!')
            break