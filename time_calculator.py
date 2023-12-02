def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Splitting the start time and converting it to 24-hour format
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    if period == "PM":
        start_hour += 12
