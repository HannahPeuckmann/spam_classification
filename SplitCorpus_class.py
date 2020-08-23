# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 23.08.20
# programm to split enron spam corpus in test, develop and train

import os

from pathlib import Path

from sklearn.model_selection import train_test_split

from collections import namedtuple

import pandas as pd

class SplitCorpus:
    def __init__(self, corpus, split_corpus):
        self.process_corpus(corpus, split_corpus)

    def process_corpus(self, corpus, split_directory): # hier eventuell noch all_ham/spam als argument übergeben
        '''writes all paths of ham and spam files of the enron email
        corpus in two csv files, named 'all_spam' and 'all_ham' '''
        all_spam = open(split_directory + '/all_spam.csv', mode='w')
        all_spam.write('file, class \n')
        all_ham = open(split_directory + '/all_ham.csv', mode='w')
        all_ham.write('file, class \n')
        for part in os.listdir(corpus):
            for spam_file in os.listdir(os.path.join(corpus, part, 'spam')):
                path = os.path.join(corpus, part, 'spam', spam_file)
                all_spam.write(path + ',' + 'spam' +'\n')
            for ham_file in os.listdir(os.path.join(corpus, part, 'ham')):
                path = os.path.join(corpus, part, 'ham', ham_file)
                all_ham.write(path + ',' + 'ham' + '\n')
        all_ham.close()
        all_spam.close()
        self.join_sets(split_directory + '/all_ham.csv', split_directory + '/all_spam.csv', split_directory)


    def split_corpus(self, data):
        ''' splits a csv file in to train (70%), validation (10%) and test (20%).
            returnes the chunks as namedtuple (train, val, test)'''
        chunks = namedtuple('chunks', 'train val test')
        all_data = pd.read_csv(data)
        train_val, test = train_test_split(all_data, test_size=0.2, random_state=42, shuffle=True)
        train, val = train_test_split(train_val, test_size=0.1, random_state=42,shuffle=True)
        return chunks(train, val, test)

    def join_sets(self, ham_set, spam_set, split_directory):
        ham_split = self.split_corpus(ham_set)
        spam_split = self.split_corpus(spam_set)
        train = pd.concat([ham_split.train, spam_split.train], ignore_index=True, sort=False)
        train.to_csv(split_directory + '/train.csv', header=False, index=False)
        val = pd.concat([ham_split.val, spam_split.val], ignore_index=True, sort=False)
        val.to_csv(split_directory + '/val.csv',header=False, index=False)
        test = pd.concat([ham_split.test, spam_split.test], ignore_index=True, sort=False)
        test.to_csv(split_directory + '/test.csv', header=False, index=False)
