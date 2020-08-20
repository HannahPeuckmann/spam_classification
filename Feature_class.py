# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.08.20
# class to extract features for single txt file


from collections import namedtuple

import logging



class Features:
    def __init__(self, file):
        f = open(file, encoding='iso-8859-2', mode='r')
        self.full_text = ''
        for line in f:
            # no f.read(), get rid of \n
            line = line.strip()
            self.full_text = self.full_text + ' ' + line
        f.close()
        features = namedtuple('features', 'uppercase special_chars hyphens whitespace')
        # create namedtuple of returnvalues
        self.features = features(*self.extract_features())
        self.normalised_features = features(*self.normalise_features())
        logging.debug(self.features)

    ### brauch i net, hier schon normalisieren?
    def extract_features(self):
        '''iterates over eacht character,
           counts whitespace, hyphens, special characters and uppercase letters
           returns absolut values '''
        count_up = 0
        count_special = 0
        count_white = 0
        count_hyphens = 0
        for char in self.full_text:
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

    def normalise_features(self):
        '''normalises absolut features by total number of characters '''
        if self.features:
            chars = len(self.full_text)
            return self.features.uppercase/chars, \
                   self.features.special_chars/chars, \
                   self.features.hyphens/chars, \
                   self.features.whitespace/chars




if __name__ == "__main__":
    logging.basicConfig(filename='Features_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    test = Features('0006.2003-12-18.GP.spam.txt')
    test.extract_features()