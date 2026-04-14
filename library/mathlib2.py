import math

def find_number_of_combination(number_of_flavours):
    # math.pow(base, exponent) returns a float, 
    # so we convert it to an int for a "count" of combinations.
    total_combination = int(math.pow(2, number_of_flavours))
    
    return total_combination

# Provide different values for number_of_flavours and test your program
number_of_combination = find_number_of_combination(6)
print(number_of_combination)