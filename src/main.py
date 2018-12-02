import preprocessing
import ngrams
import output
import os
import time


def get_queries(filename):
    with open(os.path.abspath(os.path.join(os.getcwd(), "../input/", filename))) as file:
        return file.readlines()


while True:

    option = input("\n\n1. Create unigrams\n"
                   "2. Query unigrams\n"
                   "3. Create bigrams\n"
                   "4. Query bigrams\n"
                   "5. Create trigrams\n"
                   "6. Query trigrams\n"
                   "7. Run set of 30 queries\n")

    # Create unigrams
    if option == "1":
        # English unigrams
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_unigram = ngrams.get_unigram(english_text)
        output.write_model(sorted(english_unigram.items()), "unigramEN.txt")

        # French unigrams
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_unigram = ngrams.get_unigram(french_text)
        output.write_model(sorted(french_unigram.items()), "unigramFR.txt")

        # German unigrams
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_unigram = ngrams.get_unigram(german_text)
        output.write_model(sorted(german_unigram.items()), "unigramOT.txt")

        # Welsh unigrams
        welsh_text = preprocessing.get_training_text("trainCY.txt")
        welsh_unigram = ngrams.get_unigram(welsh_text)
        output.write_model(sorted(welsh_unigram.items()), "unigramCY.txt")

        print("Unigrams created!\n")

    # Query unigrams
    elif option == "2":
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_unigram = ngrams.get_unigram(english_text)
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_unigram = ngrams.get_unigram(french_text)
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_unigram = ngrams.get_unigram(german_text)
        welsh_text = preprocessing.get_training_text("trainCY.txt")
        welsh_unigram = ngrams.get_unigram(welsh_text)

        query = input("Enter your query:\n")
        query_number = input("Enter the number of the query:\n")
        print(ngrams.query_unigram(query.lower(), english_unigram, french_unigram, german_unigram, welsh_unigram,
                                       "out" + str(query_number) + ".txt"))

    # Create bigrams
    if option == "3":
        # English bigrams
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_bigram = ngrams.get_bigram(english_text)
        output.write_model(sorted(english_bigram.items()), "bigramEN.txt")

        # French bigrams
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_bigram = ngrams.get_bigram(french_text)
        output.write_model(sorted(french_bigram.items()), "bigramFR.txt")

        # German bigrams
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_bigram = ngrams.get_bigram(german_text)
        output.write_model(sorted(german_bigram.items()), "bigramOT.txt")

        # Welsh bigrams
        welsh_text = preprocessing.get_training_text("trainCY.txt")
        welsh_bigram = ngrams.get_bigram(welsh_text)
        output.write_model(sorted(welsh_bigram.items()), "bigramCY.txt")

        print("Bigrams created!\n")

    # Query bigrams
    elif option == "4":
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_bigram = ngrams.get_bigram(english_text)
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_bigram = ngrams.get_bigram(french_text)
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_bigram = ngrams.get_bigram(german_text)
        welsh_text = preprocessing.get_training_text("trainCY.txt")
        welsh_bigram = ngrams.get_bigram(welsh_text)

        query = input("Enter your query:\n")
        query_number = input("Enter the number of the query:\n")
        print(ngrams.query_bigram(query.lower(), english_bigram, french_bigram, german_bigram, welsh_bigram,
                                   "out" + str(query_number) + ".txt"))

    # Create trigrams
    elif option == "5":
        # English trigram
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_trigram = ngrams.get_trigram(english_text)
        output.write_model(sorted(english_trigram.items()), "trigramEN.txt")

        # French trigram
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_trigram = ngrams.get_trigram(french_text)
        output.write_model(sorted(french_trigram.items()), "trigramFR.txt")

        # German trigram
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_trigram = ngrams.get_trigram(german_text)
        output.write_model(sorted(german_trigram.items()), "trigramOT.txt")

        # Welsh trigrams
        welsh_text = preprocessing.get_training_text("trainCY.txt")
        welsh_trigram = ngrams.get_trigram(welsh_text)
        output.write_model(sorted(welsh_trigram.items()), "trigramCY.txt")

        print("Trigrams created!\n")

    # Query trigrams
    elif option == "6":
        english_text = preprocessing.get_training_text("trainEN.txt")
        english_trigram = ngrams.get_trigram(english_text)
        french_text = preprocessing.get_training_text("trainFR.txt")
        french_trigram = ngrams.get_trigram(french_text)
        german_text = preprocessing.get_training_text("trainOT.txt")
        german_trigram = ngrams.get_trigram(german_text)
        welsh_text = preprocessing.get_training_text("trainCY.txt")
        welsh_trigram = ngrams.get_trigram(welsh_text)

        query = input("Enter your query:\n")
        query_number = input("Enter the number of the query:\n")
        print(ngrams.query_trigram(query.lower(), english_trigram, french_trigram, german_trigram, welsh_trigram,
                                  "out" + str(query_number) + ".txt"))


    # Run set of 30 queries
    elif option == "7":
        english_text = preprocessing.get_training_text("trainEN.txt")

        start_time = time.time()
        english_unigram = ngrams.get_unigram(english_text)
        print("EN unigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        english_bigram = ngrams.get_bigram(english_text)
        print("EN bigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        english_trigram = ngrams.get_trigram(english_text)
        print("EN trigram built in: %s seconds" % (time.time() - start_time))

        french_text = preprocessing.get_training_text("trainFR.txt")

        start_time = time.time()
        french_unigram = ngrams.get_unigram(french_text)
        print("FR unigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        french_bigram = ngrams.get_bigram(french_text)
        print("FR bigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        french_trigram = ngrams.get_trigram(french_text)
        print("FR trigram built in: %s seconds" % (time.time() - start_time))

        german_text = preprocessing.get_training_text("trainOT.txt")

        start_time = time.time()
        german_unigram = ngrams.get_unigram(german_text)
        print("GE unigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        german_bigram = ngrams.get_bigram(german_text)
        print("GE bigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        german_trigram = ngrams.get_trigram(german_text)
        print("GE trigram built in: %s seconds" % (time.time() - start_time))

        welsh_text = preprocessing.get_training_text("trainCY.txt")

        start_time = time.time()
        welsh_unigram = ngrams.get_unigram(welsh_text)
        print("CY unigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        welsh_bigram = ngrams.get_bigram(welsh_text)
        print("CY bigram built in: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        welsh_trigram = ngrams.get_trigram(welsh_text)
        print("CY trigram built in: %s seconds" % (time.time() - start_time))

        unigram_avg_time = 0
        bigram_avg_time = 0
        trigram_avg_time = 0

        # Run all queries on ngrams
        for i, query in enumerate(get_queries("queries.txt")):

            print("\nQUERY " + str(i+1) + ": " + query)

            start_time = time.time()
            print(ngrams.query_unigram(query.lower(), english_unigram, french_unigram, german_unigram, welsh_unigram,
                                       "out" + str(i + 1) + ".txt"))
            print("Unigram query ran in: %s seconds" % (time.time() - start_time))
            end_time = time.time() - start_time
            unigram_avg_time += end_time

            start_time = time.time()
            print(ngrams.query_bigram(query.lower(), english_bigram, french_bigram, german_bigram, welsh_bigram,
                                      "out" + str(i + 1) + ".txt"))
            print("Bigram query ran in: %s seconds" % (time.time() - start_time))
            end_time = time.time() - start_time
            bigram_avg_time += end_time

            start_time = time.time()
            print(ngrams.query_trigram(query.lower(), english_trigram, french_trigram, german_trigram, welsh_trigram,
                                       "out" + str(i + 1) + ".txt"))
            print("Trigram query ran in: %s seconds" % (time.time() - start_time))
            end_time = time.time() - start_time
            trigram_avg_time += end_time

        print("\nUnigram average time: %s seconds" % str(unigram_avg_time/30))
        print("Bigram average time: %s seconds" % str(bigram_avg_time/30))
        print("Trigram average time: %s seconds" % str(trigram_avg_time/30))

