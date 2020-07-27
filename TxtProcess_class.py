# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.06.20
# class to process the enron e-mail corpus

import spacy

import nltk

import logging

from collections import namedtuple


# multiprocessing!


class BasicNLP:
    def __init__(self,filename):
        self.model = spacy.load('en_core_web_sm')
        self.sentences = None
        self.tokens = []
        self.tags = []
        self.lemma = []
        f = open(filename, mode='r')
        self.full_text = ''
        for line in f:
            line = line.strip()
            self.full_text = self.full_text + ' ' + line
        f.close()

    def basic_process_file(self):
        self.sentences = [sentence for sentence in nltk.sent_tokenize(self.full_text)]
        for sentence in self.sentences:
            spacy_sentence = self.model(sentence)
            self._process_sentence(spacy_sentence)

    def _process_sentence(self, sentence):
        # tokens
        self.tokens.append([token.text for token in sentence])
        logging.debug(self.tokens)
        # tags
        self.tags.append([token.tag_ for token in sentence])
        logging.debug(self.tags)
        # lemmas
        self.lemma.append([token.lemma_ for token in sentence])
        logging.debug(self.lemma)

    def write_to_file(self, filename):
        with open(filename, mode='w') as file:
            for j in range(len(self.tokens)):
                for i in range(len(self.tokens[j])):
                    file.write(self.tokens[j][i] + '\t' + self.tags[j][i] + '\t' + self.lemma[j][i] + '\n')
                file.write('\n')

def extract_features(text):
    count_up = 0
    count_special = 0
    count_white = 0
    count_hyphens = 0
    for char in text:
        if char.isupper():
            count_up += 1
        if not char.isalpha():
            if char.isspace():
                count_white += 1
            else:
                count_special += 1
                if char == '-':
                    count_hyphens += 1
    return count_up, count_special, count_hyphens, count_white



def write_features(filename, text):
    features = namedtuple('features', 'uppercase whitespace hyphens special_chars')
    with open(filename, mode='w') as csv:
        features = features(*extract_features(text))
        csv.write(features.uppercase)



if __name__ == "__main__":
    logging.basicConfig(filename='enron_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    test = BasicNLP('0006.2003-12-18.GP.spam.txt')
    test.basic_process_file()
    test.write_to_file('Data/enron_ttl_testdata/ttl_spam_test/0006.2003-12-18.GP.spam.txt')
    logging.debug(extract_features(test.full_text))
    logging.debug(write_features('csv_filename.csv', test.full_text))
