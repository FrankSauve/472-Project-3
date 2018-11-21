import preprocessing
import ngrams
import output

while True:
    option = input("1. Create unigrams\n"
                   "2. Query unigrams\n")

    # Create unigrams
    if option == "1":
        # English unigrams
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_unigram = ngrams.get_unigram(english_text)
        output.write_unigram_model(sorted(english_unigram.items()), "unigramEN.txt")

        # French unigrams
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_unigram = ngrams.get_unigram(french_text)
        output.write_unigram_model(sorted(french_unigram.items()), "unigramFR.txt")

        # German unigrams
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_unigram = ngrams.get_unigram(german_text)
        output.write_unigram_model(sorted(german_unigram.items()), "unigramOT.txt")

        print("Unigrams created!\n")

    elif option == "2":

        english_text = preprocessing.get_training_text("trainEN.txt")
        english_unigram = ngrams.get_unigram(english_text)
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_unigram = ngrams.get_unigram(french_text)
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_unigram = ngrams.get_unigram(german_text)

        query = input("Enter your query:\n")
        query_number = input("Enter the number of the query:\n")
        print(ngrams.query_unigram(query.lower(), english_unigram, french_unigram, german_unigram,
                                   "out" + str(query_number) + ".txt"))

