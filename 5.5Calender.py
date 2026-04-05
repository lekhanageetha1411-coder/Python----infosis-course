import calendar

while True:

    year = int(input("Enter a year greater than 2000: "))

    if year > 2000:

        month = int(input("Enter a month (1-12): "))

        if 1 <= month <= 12:
            print(calendar.month(year, month))
            break
        else:
            print("Invalid month")

    else:
        print("Please enter a proper year")
