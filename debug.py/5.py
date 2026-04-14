def encode(message):
    if not message:
        return ""
    
    encoded_string = ""
    count = 1
    
    # Iterate through the string starting from the second character
    for i in range(1, len(message)):
        # If current character is same as the previous one, increment count
        if message[i] == message[i-1]:
            count += 1
        else:
            # If character changes, append the count and previous character
            encoded_string += str(count) + message[i-1]
            count = 1 # Reset count for the new character
            
    # Append the last character and its count after the loop ends
    encoded_string += str(count) + message[-1]
    
    return encoded_string

# Test cases
print(encode("AAAABBBBCCCCCCCC")) # Output: 4A4B8C
print(encode("AABCCA"))           # Output: 2A1B2C1A
print(encode("ABBBBCCCCCCCCAB"))  # Output: 1A4B8C1A1B