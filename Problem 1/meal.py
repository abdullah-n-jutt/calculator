def main():
    # Prompt the user for a time
    time_str = input("Enter the time in 24-hour format (e.g., 7:00, 13:30): ").strip()

    # Convert the time to hours as a float
    time_float = convert(time_str)

    # Determine the meal time
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    # Convert the time to hours as a float
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()
