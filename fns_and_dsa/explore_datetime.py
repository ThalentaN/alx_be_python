# File: fns_and_dsa/explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # return it in case it’s needed for further calculations

def calculate_future_date(current_date, days_to_add):
    """
    Calculate the future date by adding the specified number of days to current_date.
    
    Parameters:
    - current_date: datetime object representing the current date.
    - days_to_add: int, number of days to add.
    
    Prints the future date in YYYY-MM-DD format.
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days_input = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(current_date, days_input)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
