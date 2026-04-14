def translate(bilingual_dict, english_words_list):
    swedish_words_list = []
    
    for word in english_words_list:
        # Look up the English word in the dictionary to get the Swedish equivalent
        swedish_word = bilingual_dict[word]
        # Add the translated word to our result list
        swedish_words_list.append(swedish_word)

    return swedish_words_list

# Setup data
bilingual_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list = ["merry", "christmas"]

print("The bilingual dict is:", bilingual_dict)
print("The english words are:", english_words_list)

# Function call
swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:", swedish_words_list)