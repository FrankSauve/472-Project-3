import math
import os


def get_unigram(words):
    """
    Create a unigram model for the words provided
    :param words: List of words
    :return: sorted unigram
    """
    unigram = {}
    for word in words:
        for char in word:
            # If character is not in unigram yet, create new dictionary key
            if char not in unigram:
                unigram[char] = 1
            # Else if it already exists, increment letter frequency by one
            else:
                unigram[char] += 1

    # Calculate probability of each letter
    for c in unigram:
        unigram[c] = unigram[c]/len(words)

    return unigram


def query_unigram(query, english_unigram, french_unigram, german_unigram, output_file):
    """
    Query on unigrams to find the most probable language
    :param query: The text query
    :param english_unigram:
    :param french_unigram:
    :param german_unigram:
    :return:
    """
    # Dictionary of log probabilities of each language
    log_probs = {
        'EN': 0,
        'FR': 0,
        'GE': 0
    }
    file = open(os.path.abspath(os.path.join(os.getcwd(), "../query_output/", output_file)), "w+")
    file.write(query + "\n\n" + "UNIGRAM MODEL:\n\n")
    # Loop through all characters of the query
    for c in query:
        # If c is not an empty space
        if c != " ":
            # Add the log base 10 probability
            log_probs['EN'] += math.log(english_unigram[c], 10)
            log_probs['FR'] += math.log(french_unigram[c], 10)
            log_probs['GE'] += math.log(german_unigram[c], 10)

            file.write("UNIGRAM: " + c + "\n"
                        "FRENCH: P(" + c + ") = " + str(log_probs['FR']) + "\n" +
                        "ENGLISH: P(" + c + ") = " + str(log_probs['EN']) + "\n" +
                        "GERMAN: P(" + c + ") = " + str(log_probs['GE']) + "\n\n")

    # Sort the languages by log probability
    sorted_by_value = sorted(log_probs.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_by_value[0]


