# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.06.20
# class to process the enron e-mail corpus

import nltk

import logging


class TxtNLP:
    def __init__(self,filename):
        self.sentences = None
        self.tokens = None
        self.pos_tags = None
        self.nlp_dict = []  # List that contains a dict for each sentence,
        # every token of the sentence is a key, the value is a (named) tuple (or list?),
        # storing tag, and lemma
        f = open(filename, mode='r')
        self.full_text = ''
        for line in f:
            line = line.strip()
            self.full_text = self.full_text + ' ' + line
        f.close()

    def sentence_split(self):
        self.sentences = nltk.sent_tokenize(self.full_text,language='english')
        logging.debug(self.sentences)
        return

    def tokenize(self):
        self.tokens = [nltk.tokenize.word_tokenize(sentence, language='english') for sentence in self.sentences]
        logging.debug(self.tokens)
        return

    def tagging(self):
        self.pos_tags = [nltk.pos_tag(tokens) for tokens in self.tokens]
        logging.debug(self.pos_tags)
        return
    
    def write(self, filename):
        with open(filename, mode='w') as file:
            for sentence in self.pos_tags:
                for token, tag in sentence:
                    file.write(token + '\t' + tag + '\n')
                file.write('\n')


if __name__ == "__main__":
    logging.basicConfig(filename='enron_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    test = TxtNLP('0006.2003-12-18.GP.spam.txt')
    test.sentence_split()
    test.tokenize()
    test.tagging()
    test.write('nlp_processed.txt')
