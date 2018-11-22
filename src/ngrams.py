import math
import os


def get_unigram(words):
    """
    Create a unigram model for the words provided
    :param words: List of words
    :return: sorted unigram
    """
    alpha = 0.5
    char_total = 0
    unigram = {}
    for word in words:
        for char in word:
            # If character is not in unigram yet, create new dictionary key
            if char not in unigram:
                unigram[char] = 1 + alpha
                char_total += 1 + alpha
            # Else if it already exists, increment letter frequency by one
            else:
                unigram[char] += 1
                char_total += 1

    # Calculate probability of each letter
    for c in unigram:
        unigram[c] = unigram[c]/char_total

    return unigram

def get_bigram_v1(words):
    """
    Create a bigram model for the words provided
    :param words: List of words
    :return: sorted bigram not taking into account word endings
    """
    bigram = {}

    # TODO: Implement bigram version without taking into account word endings

    return bigram

def get_bigram_v2(words):
    """
    Create a bigram model for the words provided
    :param words: List of words
    :return: sorted bigram taking into account word endings
    """
    alpha = 0.5
    bigram_total = 0
    bigram = {}
    for word in words:
        i = 0
        while i < len(word) - 1:
            # If character is not in bigram yet, create new dictionary key
            if str(word[i]+word[i+1]) not in bigram:
                bigram[str(word[i]+word[i+1])] = 1 + alpha
                bigram_total += 1 + alpha
            # Else if it already exists, increment letter frequency by one
            else:
                bigram[str(word[i]+word[i+1])] += 1
                bigram_total += 1
            i += 1

    # TODO: Find un-used char combinations and add 0.5 (add +0.5 to bigram_total as well)

    # Calculate probability of each letter
    for c in bigram:
        bigram[c] = bigram[c]/bigram_total

    return bigram


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


def query_bigram(query, english_bigram, french_bigram, german_bigram, output_file):
    """
    Query on bigrams to find the most probable language
    :param query: The text query
    :param english_bigram:
    :param french_bigram:
    :param german_bigram:
    :return:
    """
    # Dictionary of log probabilities of each language
    log_probs = {
        'EN': 0,
        'FR': 0,
        'GE': 0
    }
    file = open(os.path.abspath(os.path.join(os.getcwd(), "../query_output/", output_file)), "w+")
    file.write(query + "\n\n" + "BIGRAM MODEL:\n\n")
    # Loop through all characters of the query

    i = 0
    while i < len(query)-1:
        c = str(query[i]+query[i+1])
        # If c is not an empty space
        if " " not in c:
            # Add the log base 10 probability
            if english_bigram[c] is not None:  #TODO: Figure out how to deal with non-existent uni/bigrams found in a query
                log_probs['EN'] += math.log(english_bigram[c], 10)
            if french_bigram[c] is not None:
                log_probs['FR'] += math.log(french_bigram[c], 10)
            if german_bigram[c] is not None:
                log_probs['GE'] += math.log(german_bigram[c], 10)

            file.write("BIGRAM: " + c + "\n"
                        "FRENCH: P(" + c + ") = " + str(log_probs['FR']) + "\n" +
                        "ENGLISH: P(" + c + ") = " + str(log_probs['EN']) + "\n" +
                        "GERMAN: P(" + c + ") = " + str(log_probs['GE']) + "\n\n")
        i += 1

    # Sort the languages by log probability
    sorted_by_value = sorted(log_probs.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_by_value[0]


