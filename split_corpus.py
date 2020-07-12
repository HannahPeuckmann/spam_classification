# programm to split enron spam corpus in test, develop and train

import os

from pathlib import Path

from sklearn.model_selection import train_test_split

import pandas as pd

def full_corpus(corpus):
    all_spam = open('all_spam.csv', mode='w')
    all_ham = open('all_ham.csv', mode='w')
    for part in os.listdir(corpus):
        for spam_file in os.listdir(os.path.join(corpus, part, 'spam')):
            path = os.path.join(corpus, part, 'spam', spam_file)
            all_spam.write(path + '\n')
        for ham_file in os.listdir(os.path.join(corpus, part, 'ham')):
            path = os.path.join(corpus, part, 'ham', spam_file)
            all_ham.write(path + '\n')
    return (all_ham, all_spam)

def split_corpus(data, setname):
    all_data = pd.read_csv(data)
    train_val, test = train_test_split(all_data, test_size=0.2, random_state=42, shuffle=True)
    test.to_csv('test_' + setname +'.csv', index=False)
    train, val = train_test_split(train_val, test_size=0.1, random_state=42,shuffle=True)
    train.to_csv('train_' + setname +'.csv', index=False)
    val.to_csv('val_' + setname +'.csv', index=False)


#full_corpus('../Enron_spam_corpus/enron_complete_dataset')
split_corpus('all_ham.csv', 'ham')
split_corpus('all_spam.csv', 'spam')
