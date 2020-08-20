# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 12.07.20
# programm to split enron spam corpus in test, develop and train

import os

from pathlib import Path

from sklearn.model_selection import train_test_split

from collections import namedtuple

import pandas as pd

def full_corpus(corpus): # hier eventuell noch all_ham/spam als argument übergeben
    '''writes all paths of ham and spam files of the enron email
       corpus in two csv files, named 'all_spam' and 'all_ham' '''
    all_spam = open('Data/all_spam.csv', mode='w')
    all_spam.write('file, class \n')
    all_ham = open('Data/all_ham.csv', mode='w')
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
    return (all_ham, all_spam)


def split_corpus(data):
    ''' splits a csv file in to train (70%), validation (10%) and test (20%).
        returnes the chunks as namedtuple (train, val, test)'''
    chunks = namedtuple('chunks', 'train val test')
    all_data = pd.read_csv(data)
    train_val, test = train_test_split(all_data, test_size=0.2, random_state=42, shuffle=True)
    train, val = train_test_split(train_val, test_size=0.1, random_state=42,shuffle=True)
    return chunks(train, val, test)

full_corpus('../Enron_spam_corpus/enron_complete_dataset')

def join_sets():
    ham_split = split_corpus('Data/all_ham.csv')
    spam_split = split_corpus('Data/all_spam.csv')
    train = pd.concat([ham_split.train, spam_split.train], ignore_index=True, sort=False)
    train.to_csv('Data/train.csv', header=False, index=False)
    val = pd.concat([ham_split.val, spam_split.val], ignore_index=True, sort=False)
    val.to_csv('Data/val.csv',header=False, index=False)
    test = pd.concat([ham_split.test, spam_split.test], ignore_index=True, sort=False)
    test.to_csv('Data/test.csv', header=False, index=False)

full_corpus('../Enron_spam_corpus/enron_complete_dataset')
join_sets()