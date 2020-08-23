# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.08.20
# class to extract features for single txt file


from collections import namedtuple

import logging

import nltk


class Features:
    '''Class to extract features of a textfile'''
    def __init__(self, file):
        f = open(file, encoding='iso-8859-2', mode='r')
        self.full_text = ''
        self.subject_line = f.readline().strip()
        self.full_text += self.subject_line
        for line in f:
            # no f.read(), get rid of \n
            line = line.strip()
            self.full_text = self.full_text + ' ' + line
        f.close()
        self.tokens = nltk.word_tokenize(self.subject_line)
        self.normalised_features = self.extract_character_features()
        # nouns in subject line
        self.headline_nouns = self.extract_nn(nltk.word_tokenize(self.subject_line))
        # nouns in whole text
        self.text_nouns = self.extract_nn(self.tokens)
        logging.debug(self.normalised_features)

    def extract_character_features(self):
        '''iterates over eacht character,
           counts whitespace, hyphens, special characters and exclamation marks
           returns absolut values '''
        # counters for features
        count_exclamation = 0
        count_special = 0
        count_white = 0
        count_hyphens = 0
        total_chars = len(self.full_text)
        # iterate over each character
        for char in self.full_text:
            if not char.isalpha():
                if char.isspace():
                    count_white += 1
                else:
                    count_special += 1
                    if char == '-':
                        count_hyphens += 1
                    if char == '!':
                        count_exclamation += 1
        return [count_exclamation/total_chars,
                count_special/total_chars,
                count_hyphens/total_chars,
                count_white/total_chars]

    def extract_nn(self, text):
        ''' tags a list of tokens and searches for nouns'''
        noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']
        tags = nltk.pos_tag(text)
        nouns = [x[0] for x in tags if x[1] in noun_tags]
        return nouns


if __name__ == "__main__":
    logging.basicConfig(filename='Features_log.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')
    test = Features('0006.2003-12-18.GP.spam.txt')