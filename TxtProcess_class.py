# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.06.20
# class to process the enron e-mail corpus

import spacy

import nltk

import logging

# multiprocessing!


class TxtNLP:
    def __init__(self,filename):
        self.model = spacy.load('en_core_web_sm')
        self.sentences = None
        self.tokens = []
        self.tags = []
        self.lemma = []
        f = open(filename, mode='r')
        full_text = ''
        for line in f:
            line = line.strip()
            full_text = full_text + ' ' + line
        f.close()
        self.sentences = [sentence for sentence in nltk.sent_tokenize(full_text)]
        for sentence in self.sentences:
            self.process_sentence(sentence)

    def process_sentence(self, sentence):
        process_sentences = self.model(sentence)
        # tokenize sentences
        self.tokens.append([token.text for token in process_sentences])
        logging.debug(self.tokens)
        self.tags.append([token.tag_ for token in process_sentences])
        logging.debug(self.tags)
        self.lemma.append([token.lemma_ for token in process_sentences])
        logging.debug(self.lemma)

    def write(self, filename):
        with open(filename, mode='w') as file:
            for j in range(len(self.tokens)):
                for i in range(len(self.tokens[j])):
                    file.write(self.tokens[j][i] + '\t' + self.tags[j][i] + '\t' + self.lemma[j][i] + '\n')
                file.write('\n')


if __name__ == "__main__":
    logging.basicConfig(filename='enron_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    test = TxtNLP('0006.2003-12-18.GP.spam.txt')
    #test.process()
    #test.tokenize()
    #test.tagging()
    test.write('nlp_processed.txt')
