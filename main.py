# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 28.06.20
# main function, manages nlp processing and feature extraction

from BasicNLP_class import BasicNLP

from Feature_class import Features

import logging

import os

# write function to read file and get full text?
# multiprocessing!
# move write features to main

logging.basicConfig(filename='main_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

def main():
    test_spam = open('Data/spam/test_spam.csv')
    for path in test_spam:
        path = path.strip()
        logging.debug(path)
        filename = path.split('/')[-1]
        logging.debug(filename)
        file_nlp = BasicNLP(path)
        file_nlp.basic_process_file()
        file_nlp.write_to_file('Data/enron_ttl_testdata/ttl_spam_test/' + filename)

main()
