from datetime import datetime, timedelta


def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()

    # Format and display
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

    return current_date  # Return it so main() can reuse if needed


def calculate_future_date(current_date):
    # Ask user for number of days to add
    days = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date
    future_date = current_date + timedelta(days=days)

    # Display formatted date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    # Part 1: Display current datetime
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
