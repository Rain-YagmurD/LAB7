from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)

def main():
    sentence = input("Sentence: ")

    reversed_string = reverse_string(sentence)
    capitalized_string = capitalize_words(sentence)
    cleaned_string = remove_punctuation(sentence)

    print("\n   String Analysis     ")
    print("Reversed:", reversed_string)
    print("Capitalized:", capitalized_string)

    print("\nRemoving punctuation:", cleaned_string)
    print("Character count (no spaces):", count_characters(cleaned_string))
    print("Word count:", count_words(cleaned_string))
    print("Average word length:", round(average_word_length(cleaned_string), 2))

if __name__ == "__main__":
    main()
