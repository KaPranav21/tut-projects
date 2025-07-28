def count_words_in_file(filename):
    word_counts = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                # Remove leading/trailing whitespace and lowercase
                line = line.strip().lower()
                # Split line into words (simple split by spaces)
                words = line.split()

                for word in words:
                    # Remove punctuation from word ends
                    word = word.strip(".,!?\"'()[]{}")
                    if word:  # if not empty
                        word_counts[word] = word_counts.get(word, 0) + 1

        print("Word counts:")
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage:
filename = input("Enter filename to count words: ")
count_words_in_file(filename)
