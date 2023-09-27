"""Splitting text data into tokens."""

import re

def sent_tokenize(text):
    """Split text into sentences."""
    
    # Split text by sentence delimiters (remove delimiters)
    text.strip()
    sentences = re.split(r"[.?]", text)
    
    # Remove leading and trailing spaces from each sentence
    sentences = [sentence.strip() for sentence in sentences]

    if "" in sentences:
        sentences.remove("")
    
    return sentences  # Return a list of sentences (remove blank strings)


def word_tokenize(sent):
    """Split a sentence into words."""
    
    # Split sent by word delimiters (remove delimiters)
    words = re.split(r"\s", sent)
    
    # Remove leading and trailing spaces from each word
    words = [word.strip() for word in words]

    return words  # Return a list of words (remove blank strings)


def test_run():
    """Called on Test Run."""

    text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"
    print("--- Sample text ---", text, sep="\n")
    
    sentences = sent_tokenize(text)
    print("\n--- Sentences ---")
    print(sentences)
    
    print("\n--- Words ---")
    for sent in sentences:
        print(sent)
        print(word_tokenize(sent))
        print()  # blank line for readability

if __name__ == "__main__":
    test_run()