STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        # The variable text is a list and must be changed to a string.
        text_string = str(text.readlines())
        # Iterates through a string of punctuation and replaces those characters in text_string
        # with blank strings.
        punctuation_string = "[].,':;!?\""
        for item in punctuation_string:
            text_string = text_string.replace(item, "")
        # "\n" indicating a new line is replaced with a blank string. A hyphen and a dash (that
        # look almost identical) are replaced with spaces so that the words they separate remain 
        # separated
        text_string = text_string.replace("\\n", "")
        text_string = text_string.replace("—", " ")
        text_string = text_string.replace("-", " ")
        # Replaces capital letters with lowercase.
        text_string = text_string.lower()
        # Takes the text string and turns it back into a list, which should be only words and no punctuation
        word_list = text_string.split()
        # Creates a new list of words that have filtered out all stop words
        word_list_filtered = []
        for word in word_list:
            if word not in STOP_WORDS:
                word_list_filtered.append(word)
        # Creates a new list from the list we just created that is sorted by count value in descending order
        word_list_sorted = sorted(word_list_filtered, key=word_list_filtered.count, reverse=True)
        # Creates an empty dictionary--each word in the sorted list is added to the dictionary as a key,
        # and its count as the value for that key
        word_count_dict = {}
        for word in word_list_sorted:
            word_count_dict[word] = word_list_sorted.count(word)
        # Prints each key in the dictionary, as well as its value, separated by a |. Asterisks are added to
        # each line equal to the respective key's value read as an integer.
        for word in word_count_dict:
            print(f"{word} | {word_count_dict.get(word)} {'*' * int(word_count_dict.get(word))}")            


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)