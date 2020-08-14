# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 28.06.20
# class for basic nlp processing of the enron e-mail corpus

import spacy

import nltk

import logging

# multiprocessing

class BasicNLP:
    def __init__(self,filename):
        self.model = spacy.load('en_core_web_sm')
        self.sentences = None
        self.tokens = []
        self.tags = []
        self.lemmas = []
        f = open(filename, encoding='iso-8859-2', mode='r')
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
        logging.debug(self.tokens)
        logging.debug(self.tags)
        logging.debug(self.lemmas)

    def _process_sentence(self, sentence):
        # tokens
        self.tokens.append([token.text for token in sentence])
        # tags
        self.tags.append([token.tag_ for token in sentence])
        # lemmas
        self.lemmas.append([token.lemma_ for token in sentence])

    def write_to_file(self, filename):
        with open(filename, mode='w') as file:
            for j in range(len(self.tokens)):
                for i in range(len(self.tokens[j])):
                    file.write(self.tokens[j][i] + '\t' + self.tags[j][i] + '\t' + self.lemmas[j][i] + '\n')
                file.write('\n')


if __name__ == "__main__":
    logging.basicConfig(filename='BasicNLP_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    test = BasicNLP('0006.2003-12-18.GP.spam.txt')
    test.basic_process_file()
    test.write_to_file('Data/enron_ttl_testdata/ttl_spam_test/0006.2003-12-18.GP.spam.txt')