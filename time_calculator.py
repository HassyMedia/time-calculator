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

    # Calculating the number of days passed and adjusting the hour
    days_later = end_hour // 24
    end_hour = end_hour % 24

    # Converting back to 12-hour format and determining AM/PM
    period = "AM" if end_hour < 12 else "PM"
    end_hour = end_hour if 1 <= end_hour <= 12 else end_hour - 12
    end_hour = 12 if end_hour == 0 else end_hour

    # Formatting the time string
    end_time = f"{end_hour}:{end_minute:02d} {period}"

    # Adding the day of the week if provided
    if starting_day:
        day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        end_time += f", {new_day}"

    # Adding information about the number of days later
    if days_later == 1:
        end_time += " (next day)"
    elif days_later > 1:
        end_time += f" ({days_later} days later)"

    return end_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
