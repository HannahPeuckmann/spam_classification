# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 28.06.20
# main function

from SpamClassifier_class import SpamClassifier

import logging

# multiprocessing!

logging.basicConfig(filename='main_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')


def main():
    classifier = SpamClassifier('Data/spam/train_spam.csv', 'Data/ham/train_ham.csv')
    classifier.train()
    print(classifier.predict('0006.2003-12-18.GP.spam.txt'))
    return


main()
