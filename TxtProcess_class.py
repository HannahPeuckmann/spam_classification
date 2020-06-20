# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.06.20
# class to process the enron e-mail corpus

import nltk

import logging


class TxtNLP:
    def __init__(self,filename):
        self.sentences = []
        self.nlp_dict = []  # List that contains a dict for each sentence,
        # every token of the sentence is a key, the value is a (named) tuple (or list?),
        # storing tag, and lemma
        f = open(filename, mode='r')
        self.full_text = f.read()
        f.close()

    def sentence_split(self):
        self.sentences.append(nltk.sent_tokenize(self.full_text,language='german'))
        logging.debug(self.sentences)
        return

    def tokenize(self):
        for sentence in self.sentences:
            tok_dict = dict()
            tokens = nltk.tokenize.word_tokenize(sentence,language='german')
            #for token in tokens:
            #    tok_dict[token] = None
            #self.nlp_dict.append(tok_dict)
        logging.debug(tokens)
        return

if __name__ == "__main__":
    logging.basicConfig(filename='enron_log.log',level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    test = TxtNLP('Enron_spam_corpus/enron_complete_dataset/enron1/spam/0006.2003-12-18.GP.spam.txt')
    test.sentence_split()
  #test.tokenize()

