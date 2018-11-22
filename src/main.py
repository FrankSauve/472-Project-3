import preprocessing
import ngrams
import output

while True:

    option = input("1. Create unigrams\n"
                   "2. Query unigrams\n"
                   "3. Create bigrams\n"
                   "4. Query bigrams\n")

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
    # Create bigrams
    if option == "3":
        # English bigrams
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_bigram = ngrams.get_bigram_v2(english_text)
        output.write_bigram_model(sorted(english_bigram.items()), "bigramEN.txt")

        # French bigrams
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_bigram = ngrams.get_bigram_v2(french_text)
        output.write_bigram_model(sorted(french_bigram.items()), "bigramFR.txt")

        # German bigrams
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_bigram = ngrams.get_bigram_v2(german_text)
        output.write_bigram_model(sorted(german_bigram.items()), "bigramOT.txt")

        print("Bigrams created!\n")

    elif option == "4":

        english_text = preprocessing.get_training_text("trainEN.txt")
        english_bigram = ngrams.get_bigram_v2(english_text)
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_bigram = ngrams.get_bigram_v2(french_text)
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_bigram = ngrams.get_bigram_v2(german_text)

        query = input("Enter your query:\n")
        query_number = input("Enter the number of the query:\n")
        print(ngrams.query_bigram(query.lower(), english_bigram, french_bigram, german_bigram,
                                   "out" + str(query_number) + ".txt"))

