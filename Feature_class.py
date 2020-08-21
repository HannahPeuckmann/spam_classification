# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.08.20
# class to extract features for single txt file


from collections import namedtuple

import logging

import nltk





class Features:
    def __init__(self, file):
        f = open(file, encoding='iso-8859-2', mode='r')
        self.full_text = ''
        for line in f:
            # no f.read(), get rid of \n
            line = line.strip()
            self.full_text = self.full_text + ' ' + line
        f.close()
        features = namedtuple('features', 'exclamation special_chars hyphens whitespace total_tokens pronouns')
        # create namedtuple of returnvalues
        #self.normalised_features = features(*(self.extract_character_features() + self.extract_token_features()))
        self.normalised_features = features(*(self.extract_character_features() + self.extract_token_features()))
        logging.debug(self.normalised_features)

    def extract_character_features(self):
        '''iterates over eacht character,
           counts whitespace, hyphens, special characters and uppercase letters
           returns absolut values '''
        count_exclamation = 0
        count_special = 0
        count_white = 0
        count_hyphens = 0
        total_chars = len(self.full_text)
        for char in self.full_text:
            if not char.isalpha():
                if char.isspace():
                    count_white += 1
                else:
                    count_special += 1
                    if char == '-':
                        count_hyphens += 1
                    if char =='!':
                        count_exclamation += 1
        return count_exclamation/total_chars, count_special/total_chars, count_hyphens/total_chars, count_white/total_chars

    def extract_token_features(self):
        tokens = nltk.word_tokenize(self.full_text)
        total_tokens = len(tokens)
        pronouns = 0
        for tag_pair in nltk.pos_tag(tokens):
            if tag_pair[1] == 'PRP':
                pronouns += 1
        return total_tokens, pronouns/total_tokens



if __name__ == "__main__":
    logging.basicConfig(filename='Features_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    test = Features('0006.2003-12-18.GP.spam.txt')