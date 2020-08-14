# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 28.06.20
# main function, manages nlp processing and feature extraction

from BasicNLP_class import BasicNLP

from Feature_class import Features

from operator import add

import logging

import os

# write function to read file and get full text?
# multiprocessing!

logging.basicConfig(filename='main_log.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')



def ttl_nlp():
    all_spam = open('Data/spam/train_spam.csv')
    all_ham = open('Data/ham/train_ham.csv')
    def process(data_in, setname):
        for path in data_in:
            path = path.strip()
            logging.debug(path)
            filename = path.split('/')[-1]
            file_nlp = BasicNLP(path)
            file_nlp.basic_process_file()
            file_nlp.write_to_file('Data/enron_ttl_traindata/ttl_' + setname +'_train/' + filename)
    process(all_ham, 'ham')
    process(all_spam, 'spam')
    return

def train():
    sum_features = open('Data/sum_features_extracted.csv', mode='w')
    train_feature_file = open('Data/features_extracted.csv', mode='w')
    train_spam = open('Data/spam/train_spam.csv')
    train_ham = open('Data/ham/train_ham.csv')
    def train_data(data, setname):
        sum_features = [0,0,0,0]
        for path in data:
            path = path.strip()
            feature_obj = Features(path)
            feature_obj.extract_features()
            feature_obj.normalise_features()
            sum_features = list( map(add, sum_features , list(feature_obj.normalised_features)))
            train_feature_file.write(setname
                                     + ','
                                     + str(feature_obj.normalised_features.uppercase)
                                     + ','
                                     + str(feature_obj.normalised_features.special_chars)
                                     + ','
                                     + str(feature_obj.normalised_features.hyphens)
                                     + ','
                                     + str(feature_obj.normalised_features.whitespace)
                                     + '\n'
                                     )
            return sum_features
    spam_sum = train_data(train_spam, 'spam')
    ham_sum = train_data(train_ham, 'ham')
    sum_features.write('spam' + ','
                       + str(spam_sum[0]) + ','
                       + str(spam_sum[1]) + ','
                       + str(spam_sum[2]) + ','
                       + str(spam_sum[3]) + '\n'
                       ) 
    sum_features.write('ham' + ','
                       + str(ham_sum[0]) + ','
                       + str(ham_sum[1]) + ','
                       + str(ham_sum[2]) + ','
                       + str(ham_sum[3])
                       )
    return



def main():
    train()
    return


main()
