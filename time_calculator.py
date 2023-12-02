def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Splitting the start time and converting it to 24-hour format
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    if period == "PM":
        start_hour += 12

    # Splitting the duration time
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Adding the duration to the start time
    end_hour = start_hour + duration_hours
    end_minute = start_minute + duration_minutes

    # Adjusting minutes and hours
    if end_minute >= 60:
        end_hour += end_minute // 60
        end_minute = end_minute % 60
