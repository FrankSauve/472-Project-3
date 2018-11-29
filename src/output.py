import os


def write_model(model, filename):
    """
    Write to ngrams_output file as : (letter) = prob
    :param unigram: List of (letter, prob) tuples
    :param filename: Name of the ngrams_output file
    """
    with open(os.path.abspath(os.path.join(os.getcwd(), "../ngrams_output/", filename)), "w+") as file:
        for c in model:
            letter, prob = c
            file.write("(" + letter + ") = " + str(prob) + "\n")

