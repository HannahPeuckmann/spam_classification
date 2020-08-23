# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 23.08.20
# main function

from SpamClassifier_class import SpamClassifier

from SplitCorpus_class import SplitCorpus

import logging

import sys

### to do: progress bar, unit tests, assertions?, improve docstrings


def process_corpus(modi_input):
    split_corpus = SplitCorpus(*modi_input)
    logging.info('Corpus was split into train, validation and test, saved as:')
    logging.info(modi_input[-1] + '/train.csv')
    logging.info(modi_input[-1] + '/val.csv')
    logging.info(modi_input[-1] + '/test.csv')


def train(modi_input):
    classifier = SpamClassifier()
    classifier.train(*modi_input)
    logging.info('classifier was trained, features are extracted and saved to '
                  + modi_input[1]
                  + ' and '
                  + modi_input[2])

def predict(modi_input):
    classifier = SpamClassifier(modi_input[0])
    logging.info(classifier.predict(modi_input[1]))

def evaluate(modi_input):
    classifier = SpamClassifier(modi_input[0])
    (right, wrong, total, accuracy) = classifier.evaluate(modi_input[1],
                                                          modi_input[2])
    logging.info('correct classified: ' + str(right))
    logging.info('wrong classified: ' + str(wrong))
    logging.info('accuracy: ' + str(accuracy))

def user_mode(cmd_input):
    if cmd_input[1] == '--train':
        if len(cmd_input) == 5:
            train(cmd_input[2:])
    elif cmd_input[1] == '--predict':
        if len(cmd_input) == 4:
            predict(cmd_input[2:])
    elif cmd_input[1] == '--evaluate':
        if len(cmd_input) == 5:
            evaluate(cmd_input[2:])
    elif cmd_input[1] == '--data':
        if len(cmd_input) == 4:
            process_corpus(cmd_input[2:])

if __name__ == "__main__":
    logging.basicConfig(filename='main_log.log',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')
    user_mode(sys.argv)
