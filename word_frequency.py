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
        # This list variable is initialized so we can append strings to it in the following for loop
        word_count_list = []
        # In this loop, the count method is called on word_list_filtered to count instances of a word, and
        # saved to the word_count variable as a string. The list created above has an entry appended that
        # includes the word, number of times it appears, and asterisks equal to that number. This list
        # contains duplicate entries for each time the word appears, and is not sorted.
        for word in word_list_filtered:
            word_count = str(word_list_filtered.count(word))
            word_count_list.append(f"{word} | {word_count} {'*' * int(word_count)}")
        # Sorts the list by frequency count in reverse order, so the most frequent entries are listed first
        word_count_list = sorted(word_count_list, key=word_count_list.count, reverse=True)
        # Duplicates are removed by converting the list to a set, which may not contain duplicates
        word_count_no_dupes = set(word_count_list)
        # The set is sorted using the index of its respective list as a key, as that list was already sorted
        # by frequency
        word_count_no_dupes = sorted(word_count_no_dupes, key=word_count_list.index)
        for item in word_count_no_dupes:
            print(item)
            


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