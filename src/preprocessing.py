import re
import os


def get_training_text(filename):
    """
    Returns a filtered training dataset
    :param filename: Name of the txt file with the extension
    :return: filtered_text
    """
    with open(os.path.abspath(os.path.join(os.getcwd(), "../input/", filename))) as file:
        text = file.read().replace("\n", '')  # Put the entire text into one big string
        filtered_text = re.findall("\w+", text)  # Only take the words

    return filtered_text

