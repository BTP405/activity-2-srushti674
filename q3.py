def wordCount(t):
    # Reads data from the file 't' and returns a dictionary with word occurrences.
    word_occurrences = {}

    with open(t, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                # Remove punctuation and convert to lowercase for uniformity
                cleaned_word = word.strip('.,!?()[]{}"\'').lower()

                # If the word is not in the dictionary, add it with the current line number
                if cleaned_word not in word_occurrences:
                    word_occurrences[cleaned_word] = [line_number]
                else:
                    # If the word is already in the dictionary, append the current line number
                    word_occurrences[cleaned_word].append(line_number)

    return word_occurrences


# Example usage:
file_path = 'Q3.txt'
word_occurrences = wordCount(file_path)

# Display word occurrences in the desired format
for word, occurrences in word_occurrences.items():
    print(f'{word} : {occurrences}')

