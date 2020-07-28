# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 28.06.20
# class to extract features from the enron e-mail corpus


from collections import namedtuple

import logging

# features normalisieren! -> textlänge

class Features:
    def __init__(self, file):
        f = open(file, mode='r')
        self.full_text = ''
        for line in f:
            line = line.strip()
            self.full_text = self.full_text + ' ' + line
        f.close()
        features = namedtuple('features', 'uppercase special_chars hyphens whitespace')
        self.features = features(*self.extract_features())
        logging.debug(self.features)

    def extract_features(self):
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



    def write_features(self, filename):
        with open(filename, mode='w') as csv:
            csv.write(str(self.features.uppercase)
                    + ','
                    + str(self.features.special_chars)
                    + ','
                    + str(self.features.hyphens)
                    + ','
                    + str(self.features.whitespace)
                    )
        return

if __name__ == "__main__":
    logging.basicConfig(filename='Features_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    test = Features('0006.2003-12-18.GP.spam.txt')
    test.extract_features()