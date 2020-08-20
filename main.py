# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.08.20
# main function

from SpamClassifier_class import SpamClassifier

import logging

logging.basicConfig(filename='main_log.log',level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')



def main():
    classifier = SpamClassifier('Data/sum_features_extracted.csv')
    print(classifier.evaluate('Data/val.csv', 'Data/predictions.csv'))
    return

if __name__ == "__main__":
    main()
