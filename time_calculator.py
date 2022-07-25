def add_time(start, duration, day=""):
    # Slicing the strings of first two arguments and converting them to integer
    start_string = start.split(":")
    hour1 = int(start_string[0])
    min1 = int(start_string[1].split(" ")[0])
    hour2 = int(duration.split(":")[0])
    min2 = int(duration.split(":")[1])

    # Calculations for multiple days
    day_count = int(hour2 / 24)
    hour2 -= day_count * 24

    # Initial calculations
    hour_result = hour1 + hour2
    min_result = min1 + min2

    # AM and PM
    meridiem = start_string[1].split(" ")[1]

    next_day = None

    # If day argument is given (argument is case insensitive)
    if day:
        day = day.casefold()
        day = day.capitalize()
        days = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4,
                "Friday": 5, "Saturday": 6, "Sunday": 7}
        day_index = days.get(day)

    # Add hours if minutes more than 60
    if min_result >= 60:
        hour_result = hour_result + int(min_result / 60)
        min_result = min_result - 60

    # Minute formatting below 10 minutes (for example 5:04)
    if min_result < 10:
        min_result = f"0{min_result}"

    # PM to AM and vice versa
    if meridiem == "PM" and hour_result > 12:
        hour_result = hour_result - 12
        meridiem = "AM"
        next_day = "(next day)"
        day_count += 1

    # 12:00 (midnight)
    elif meridiem == "PM" and hour_result == 12:
        meridiem = "AM"
        next_day = "(next day)"
        day_count += 1

    elif meridiem == "AM" and hour_result > 12:
        hour_result = hour_result - 12
        meridiem = "PM"

    # 12:00 (noon)
    elif meridiem == "AM" and hour_result == 12:
        meridiem = "PM"

    # We do not want output like 0:45 but 12:45 when sum of hours is zero
    if hour_result == 0:
        hour_result += 12

    # Checking that we do not get weird output like 15:15 AM
    if hour_result > 12:
        hour_result -= 12

    # If only 1 day passes it says "(next day)"
    if day_count == 1:
        next_day = "(next day)"
        if day != "":
            day_index += 1

    # Adding a counter for days passed
    if day_count > 1:
        next_day = f"({day_count} days later)"
        if day != "":
            day_index += day_count
            # Retrieving the correct day
            if day_count % 7 == 0:
                day_index = day_index - day_count
            else:
                day_index = day_index - day_count + day_count % 7
                if day_index > 7:
                    day_index -= 7

    # Standard output (no days passed)
    new_time = f"{hour_result}:{min_result} {meridiem}"

    # Find the new day from dictionary
    if day:
        day = list(days.keys())[list(days.values()).index(day_index)]

    # Final output formatting
    if next_day is None and day != "":
        return new_time + ", " + day
    elif next_day is not None and day != "":
        return new_time + ", " + day + " " + next_day
    elif next_day is None:
        return new_time
    else:
        return new_time + " " + next_day
