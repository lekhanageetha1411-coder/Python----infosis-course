def check_palindrome(word):
    # We use slicing [::-1] to create a reversed copy of the string
    # Then we compare it to the original word
    if word == word[::-1]:
        return True
    
    return False

# Testing the function
status = check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")