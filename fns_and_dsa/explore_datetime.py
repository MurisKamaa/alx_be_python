from datetime import datetime, timedelta

def display_current_datetime():
    date_now = datetime.now()
    return "Current date and time:", date_now.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days):
    days = input("Enter the number of days to add to the current date: ")
    date_now = datetime.now()
    future_date = date_now + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")