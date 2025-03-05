import re
from collections import Counter

def word_frequencies(text):
    """
    Counts the frequency of each word in a given text and returns a dictionary sorted by frequency.

    :param text: Input string containing words
    :return: Dictionary with words as keys and their counts as values, sorted in descending order
    """
    # Converting text to lowercase to ensure case-insensitive counting
    text = text.lower()
    
    # Using regex to extract words from the text
    # \b\w+\b matches complete words:
    #   - \b ensures I match a whole word boundary
    #   - \w+ matches one or more word characters (letters, digits, underscore)
    #   - \b ensures I don't match partial words or punctuation
    words = re.findall(r'\b\w+\b', text)
    
    # Counting occurrences of each word using Counter from collections
    word_count = Counter(words)
    
    # Sorting words by frequency in descending order
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_word_count

# Test cases
test_cases = [
    "Hello world! This is a test. Hello, this test is only a test.",  # Original case
    "Python is fun. Python, Python, Python! Fun is coding in Python.",  # Repeated word
    "One, two, two. Three, three, three!",  # Different word frequencies
    "CASE case CaSe casE.",  # Case insensitivity test
    "Wow! Wow? wow... wow, WOW!!",  # Punctuation handling
    "Let's see how contractions work: don't, can't, it's, isn't.",  # Contractions test
]

# Running test cases
for i, text in enumerate(test_cases, 1):
    print(f"\nTest Case {i}: {text}")
    frequencies = word_frequencies(text)
    print("Word Frequencies:")
    for word, count in frequencies.items():
        print(f"{word}: {count}")
