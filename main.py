# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 30.08.20
# main function

from SpamClassifier_class import SpamClassifier

from SplitCorpus_class import SplitCorpus

import logging

import sys



class InputError(Exception):
    '''Exception for errors in the user input.'''

    def __init__(self, message):
        self.message = message


def process_corpus(modi_input):
    SplitCorpus(*modi_input)
    logging.info('Corpus was split into train, validation and test, saved as:')
    logging.info(modi_input[-1] + '/train.csv')
    logging.info(modi_input[-1] + '/val.csv')
    logging.info(modi_input[-1] + '/test.csv')


def train(modi_input):
    classifier = SpamClassifier()
    classifier.train(*modi_input)
    print('finished training')
    logging.info('classifier was trained, features are extracted and saved to '
                  + modi_input[1]
                  + ' and '
                  + modi_input[2])

def predict(modi_input):
    classifier = SpamClassifier(modi_input[0])
    logging.info(classifier.predict(modi_input[1]))

def evaluate(modi_input):
    classifier = SpamClassifier(modi_input[0])
    (right, wrong,_ , accuracy) = classifier.evaluate(modi_input[1],
                                                          modi_input[2])
    logging.info('correct classified: ' + str(right))
    logging.info('wrong classified: ' + str(wrong))
    logging.info('accuracy: ' + str(accuracy))
    print('finished evaluating.\npredictions are saved at:\n'
          + modi_input[2])

def user_mode(cmd_input):
    ''' Parses the user input, raises an error for wrong input. 
        Identifies the intended user mode and selects the corresponding function '''
    # Error message
    synopsis = 'Invalid Input! Propper usage:\n'\
                        + '$ python3 main.py --data KORPUS_DIRECTORY KORPUS_SPLIT_DIRECTORY \n'\
                        + '$ python3 main.py --train KORPUS_CSV CLASS_FEATURE_CVS SINGLE_MAIL_FEATURE_CSV \n'\
                        + '$ python3 main.py --predict CLASS_FEATURE_CSV MAIL_FILE \n'\
                        + '$ python3 main.py --evaluate CLASS_FEATURE_CSV TEST_KORPUS_CSV PREDICTIONS.CSV \n'\
                        + 'See the README for more details.\n'

    if cmd_input[1] == '--train':
        if len(cmd_input) == 5:
            train(cmd_input[2:])
        else:
            raise InputError(synopsis)
    elif cmd_input[1] == '--predict':
        if len(cmd_input) == 4:
            predict(cmd_input[2:])
        else:
            raise InputError(synopsis)
    elif cmd_input[1] == '--evaluate':
        if len(cmd_input) == 5:
            evaluate(cmd_input[2:])
        else:
            raise InputError(synopsis)
    elif cmd_input[1] == '--data':
        if len(cmd_input) == 4:
            process_corpus(cmd_input[2:])
        else:
            raise InputError(synopsis)
    else:
        raise InputError(synopsis)

if __name__ == "__main__":
    logging.basicConfig(filename='main_log.log',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')
    user_mode(sys.argv)
