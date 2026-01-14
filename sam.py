from datetime import datetime

def calculate_age():
    """Calculate age from birth date"""
    print("=== Age Calculator ===\n")

    print("=== Age Calculator ===\n")

    
    
    try:
        # Get birth date from user
        birth_year = int(input("Enter your birth year (e.g., 1990): "))
        birth_month = int(input("Enter your birth month (1-12): "))
        birth_day = int(input("Enter your birth day (1-31): "))
        
        # Create birth date object
        birth_date = datetime(birth_year, birth_month, birth_day)
        
        # Get current date
        current_date = datetime.now()
        
        # Calculate age
        age = current_date.year - birth_date.year
        
        # Adjust age if birthday hasn't occurred this year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        # Display result
        print(f"\nYour birth date: {birth_date.strftime('%B %d, %Y')}")
        print(f"Current date: {current_date.strftime('%B %d, %Y')}")
        print(f"Your age: {age} years old")

        print("=== Age Calculator ===\n")
        
    except ValueError:
        print("Error: Please enter valid numbers for year, month, and day.")
    except Exception as e:
        print(f"An error occurred: {e}")

        print("=== Age Calculator ===\n")

        print("=== Age Calculator ===\n")

if __name__ == "__main__":
    calculate_age()
