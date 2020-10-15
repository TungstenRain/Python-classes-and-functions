"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 16: Classes and Functiosn in Think Python 2
    
    Note: Using Python 3.9.0
"""
from datetime import datetime

def main():
    """
        Main function
    """
    # initialize variables
    today = datetime.today()
    print("Today's date and time.")
    print(today)
    print(today.strftime("%A"))

    # Request user's birthday
    str_users_birthday = input("Please enter your birhday in MM/DD/YYYY format: ")
    users_birthday = datetime.strptime(str_users_birthday, "%m/%d/%Y")

    next_birthday = users_birthday.replace(year = today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year = today.year + 1)
    print("Your next birthday is: " + str(next_birthday))

    days_to_birthday = next_birthday - today
    print(str(days_to_birthday) + " until your next birthday!")

    last_birthday = next_birthday.replace(year = next_birthday.year - 1)
    age = last_birthday.year - users_birthday.year
    print("You are %d years old" % age)

    bday1 = datetime(day=11, month=5, year=1967)
    bday2 = datetime(day=11, month=7, year=2015)
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2 - d1)
    print("For people born on these dates: ")
    print(bday1)
    print(bday2)
    print("Their double day is: ")
    print(dd)


if __name__ == "__main__":
    main()