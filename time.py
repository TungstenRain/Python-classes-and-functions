"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 16: Classes and Functions in Think Python 2
    
    Note: Using Python 3.9.0
"""
class Time:
    """
        Represents the time of day

        attributes: hour, minute, second
    """


def print_time(t):
    """
        Print the time in hh:mm:ss format

        t: Time
    """
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    """
        Determine if one time (t1) is after another time (t2)

        t1: Time
        t2: Time

        return: boolean; True if t1 is after t2; false otherwise
    """
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def add_time(t1, t2):
    """
        Add two Times together

        t1: Time
        t2: Time

        return: Time; the summation of the two times
    """
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def increment(time, seconds):
    """
        Increment the time by seconds

        time: Time
        seconds: int

        return: Time
    """
    assert valid_time(time)
    seconds += time_to_int(time)
    return int_to_time(seconds)


def valid_time(time):
    """
        Determine if a Time object satisfies the invariants

        time: Time

        return: boolean; True if satisfies the invariants, False otherwise
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def time_to_int(time):
    """
        Convert Time to int (seconds)

        time: Time

        return: int
    """
    return (((time.hour * 60) + time.minute) * 60) + time.second


def int_to_time(seconds):
    """
        Convert an int (seconds) to Time

        seconds: int

        return: Time
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)

    return time


def multiply_time(time, factor):
    """
        Multiply a time by a factor

        time: Time
        factor: int

        return: Time
    """
    assert valid_time(time)
    seconds = time_to_int(time) * factor
    return int_to_time(seconds)


def main():
    """
        Main function
    """
    print("Welcome to the rat race!")
    
    # Instantiate Time
    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 12

    print("The time it took to run the half marathon:", end=" ")
    print_time(race_time)

    distance = 13.1
    pace = multiply_time(race_time, 1/distance)

    print("The race was %g miles long." % distance)
    print("The pace (time per mile) was:", end=" ")
    print_time(pace)


if __name__ == "__main__":
    main()