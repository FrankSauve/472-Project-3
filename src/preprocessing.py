import re
import os
import unicodedata


def get_training_text(filename):
    """
    Returns a filtered training dataset
    :param filename: Name of the txt file with the extension
    :return: filtered_words
    """
    with open(os.path.abspath(os.path.join(os.getcwd(), "../input/", filename))) as file:
        text = file.read().replace("\n", '')  # Put the entire text into one big string
        words = re.findall("[a-zA-Z]+", text)  # Only take the words

        filtered_words = []
        for word in words:
            filtered_words.append(remove_accents(word))

    return filtered_words


def remove_accents(s):
    """
    Removes accents using unicode
    :param s: Input string
    :return: The input string without accents
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')
