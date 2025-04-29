"""
Student Population Growth Analysis Program
------------------------------
Author: Bryan Caban
Assignment: Chapter 13 Programming Exercise 13

Overview:
This program analyzes population growth for cities in Florida using SQLite database and matplotlib.
It provides visualization of population trends and projections over a 20-year period.
"""

import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def create_database_and_table():
    """
    Creates a database called population_CM and a table named population
    with fields for city, year, and population.
    """
    # Connect to the database (will create it if it doesn't exist)
    conn = sqlite3.connect('population_CM.db')
    cursor = conn.cursor()
    
    # Create the population table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS population (
        city TEXT,
        year INTEGER,
        population INTEGER,
        PRIMARY KEY (city, year)
    )
    ''')
    
    # Initial population data for 10 Florida cities in 2023
    cities_data = [
        ('Jacksonville', 2023, 949611),
        ('Miami', 2023, 442241),
        ('Tampa', 2023, 384959),
        ('Orlando', 2023, 307573),
        ('St. Petersburg', 2023, 258308),
        ('Hialeah', 2023, 223109),
        ('Tallahassee', 2023, 196169),
        ('Port St. Lucie', 2023, 189396),
        ('Cape Coral', 2023, 183365),
        ('Fort Lauderdale', 2023, 182760)
    ]
    
    # Insert initial data
    cursor.executemany('''
    INSERT OR IGNORE INTO population (city, year, population) VALUES (?, ?, ?)
    ''', cities_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database and table created successfully!")
    return cities_data

def simulate_population_growth(cities_data, years=20, growth_rate=0.02):
    """
    Simulates population growth for the next 20 years at a 2% growth rate
    and inserts the data into the population table.
    """

    conn = sqlite3.connect('population_CM.db')
    cursor = conn.cursor()
    
    # Get distinct cities
    cities = [city[0] for city in cities_data]
    
    # For each city, calculate and insert population for future years
    for city in cities:
        # Get the starting population from 2023
        cursor.execute('SELECT population FROM population WHERE city = ? AND year = 2023', (city,))
        start_population = cursor.fetchone()[0]
        
        # Calculate and insert population for each future year
        for year_offset in range(1, years + 1):
            year = 2023 + year_offset
            # Calculate new population with compound growth
            new_population = int(start_population * ((1 + growth_rate) ** year_offset))
            
            # Insert new population data
            cursor.execute('''
            INSERT OR REPLACE INTO population (city, year, population) 
            VALUES (?, ?, ?)
            ''', (city, year, new_population))
    
    conn.commit()
    conn.close()
    print(f"Population growth simulated for {years} years at {growth_rate*100}% annual growth rate!")
    return cities

def display_population_growth(cities):
    """
    Displays population growth for a city selected by the user.
    """
    # Display available cities
    print("\nAvailable cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")
    
    # Get user choice
    while True:
        try:
            choice = int(input("\nSelect a city (enter the number): "))
            if 1 <= choice <= len(cities):
                selected_city = cities[choice-1]
                break
            else:
                print(f"Please enter a number between 1 and {len(cities)}.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Fetch data for the selected city
    conn = sqlite3.connect('population_CM.db')
    cursor = conn.cursor()
    cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (selected_city,))
    data = cursor.fetchall()
    conn.close()
    
    # Extract years and population values
    years = [row[0] for row in data]
    population = [row[1] for row in data]
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(years, population, marker='o', linestyle='-', color='blue')
    plt.title(f'Population Growth for {selected_city} (2023-2043)')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    
    # Add a best fit line to highlight the growth trend
    z = np.polyfit(years, population, 1)
    p = np.poly1d(z)
    plt.plot(years, p(years), "r--", alpha=0.8)
    
    # Format the y-axis with commas for thousands
    plt.gca().get_yaxis().set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
    
    # Rotate x-axis labels for better readability and show only some years
    plt.xticks(years[::5], rotation=45)
    
    plt.tight_layout()
    plt.show()

def runcode():
    # Ask user if they want to run the program
    response = input("Do you want to run this code? (y/n): ")
    
    # Convert response to lowercase and check if it's 'y'
    return response.lower() == 'y'

def main():
    # Create database and initial table
    cities_data = create_database_and_table()
    
    # Simulate population growth
    cities = simulate_population_growth(cities_data)
    
    # Display population growth for a selected city
    display_population_growth(cities)

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