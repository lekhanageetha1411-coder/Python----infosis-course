def find_leap_years(given_year):
    list_of_leap_years = []

    while len(list_of_leap_years) < 15:
        # Check the leap year condition
        if (given_year % 4 == 0 and given_year % 100 != 0) or (given_year % 400 == 0):
            list_of_leap_years.append(given_year)
        
        # This MUST be outside the IF block so we move to the next year 
        # regardless of whether the current one was a leap year or not.
        given_year += 1

    # This MUST be outside the WHILE loop so it returns the full list 
    # only after the loop has found all 15 years.
    return list_of_leap_years

result_list = find_leap_years(2000)
print(result_list)