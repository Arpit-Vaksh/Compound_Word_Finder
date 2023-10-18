import time
def read_words_from_file(filename):
    words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                words.append(line.strip())
    except Exception as e:
        print("Error reading file:", e)
    return words

def is_compound_word(word, words_set):
    if len(word) == 0:
        return False
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in words_set and (suffix in words_set or is_compound_word(suffix, words_set)):
            return True
    return False

if __name__ == "__main__":
    start_time = time.time()

    words = read_words_from_file("Input_01.txt")
    words_set = set(words)

    longest_compound_word = ""
    second_longest_compound_word = ""

    for word in words:
        if is_compound_word(word, words_set):
            if len(word) > len(longest_compound_word):
                second_longest_compound_word = longest_compound_word
                longest_compound_word = word
            elif len(word) > len(second_longest_compound_word):
                second_longest_compound_word = word

    print("Longest Compound Word:", longest_compound_word)
    print("Second Longest Compound Word:", second_longest_compound_word)

    end_time = time.time()
    print("Time taken to process the input file:", (end_time - start_time), "seconds")
