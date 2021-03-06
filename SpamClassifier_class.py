# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 30.08.20
# spam classifier


import logging

import re

from operator import add, sub

from Feature_class import Features

from  progress.spinner import Spinner

from collections import namedtuple, Counter


class SpamClassifier:
    '''Class to classifie textfiles as ham or spam,
       either single mail or dataset'''
    def __init__(self, extracted_features_csv=None):
        # agregated features of ham and spam class
        # from file
        if extracted_features_csv != None:
            features = open(extracted_features_csv, mode='r')
            self.sum_features_spam = [float(x) for x in features.readline().split(',')[1:]]
            self.sum_features_ham = [float(x) for x in features.readline().split(',')[1:]]
        # or trained
        else:
            self.sum_features_ham = None
            self.sum_features_spam = None
        self.most_common_nn = None
        # Progress spinner
        self.spinner = Spinner('running ')

    def train(self, train_csv, class_features_csv, single_mail_features_csv):
        '''extracts and saves features for each file of a corpus,
           extracts and saves aggregated features of the corpus'''
        # find most common nn of spam subject lines
        self._find_most_common(train_csv)
        train_mails = open(train_csv, mode='r')
        class_features = open(class_features_csv, mode='w')
        single_mail_features = open(single_mail_features_csv, mode='w')
        # initiate counters
        sum_features_spam = sum_features_ham = [0, 0, 0, 0, 0]
        total_ham = total_spam = 0
        # feature extraction for each file
        for line in train_mails:
            self.spinner.next()
            spam_headwords = 0
            line = line.strip().split(',')
            path = line[0]
            target = line[1]
            feature_obj = Features(path)
            features = list(feature_obj.normalised_features)
            # search for spam headlines words
            for token in self.most_common_nn:
                # escaping special characters in
                token = re.escape(token)
                # only match whole tokens, no subtokens
                token = r"\b" + token + r"\b"
                matches = re.findall(token, feature_obj.full_text)
                spam_headwords += len(matches)
            # normalise
            spam_headwords = spam_headwords/len(feature_obj.full_text)
            features.append(spam_headwords)
            if target == 'spam':
                total_spam += 1
                # sums elements at the same index of the two lists
                sum_features_spam = list(map(add, sum_features_spam, features))
            else:
                total_ham += 1
                sum_features_ham = list(map(add, sum_features_ham, features))
            # safe features per mail to csv
            single_mail_features.write(target
                                + ','
                                + ','.join(map(str, features))
                                + '\n')
        # normalise class features
        self.sum_features_spam = [element/total_spam for element in sum_features_spam]
        self.sum_features_ham = [element/total_ham for element in sum_features_ham]
        # safe class features to csv
        class_features.write('spam,'
                             + ','.join(map(str, self.sum_features_spam))
                             + '\n')
        class_features.write('ham,'
                             + ','.join(map(str, self.sum_features_ham)))

    def predict(self, mail):
        '''predicts class for a single mail file,
           returns prediction and distance to predicted class'''
        feature_obj = Features(mail)
        mail_features = list(feature_obj.normalised_features)
        # compute distance to classes
        # difference between elements at the same index
        # of the two feature lists
        mail_spam_dist = sum(list(map(lambda x, y: abs(x - y),
                             mail_features, self.sum_features_spam)))
        mail_ham_dist = sum(list(map(lambda x, y: abs(x - y), mail_features,
                            self.sum_features_ham)))
        logging.debug('distance to spam class: ' + str(mail_spam_dist))
        logging.debug('distance to ham class: ' + str(mail_ham_dist))
        prediction = namedtuple('prediction', 'distance prediction')
        # predict the class
        if mail_ham_dist < mail_spam_dist:
            return prediction(mail_ham_dist, 'ham')
        else:
            return prediction(mail_spam_dist, 'spam')

    def evaluate(self, val_set_csv, predictions_file_csv):
        '''computes the accuracy of the trained classifier,
           saves gold class and predicted class to csv,
           returns the accuracy'''
        predicted_data = open(predictions_file_csv, mode='w')
        val_data = open(val_set_csv, mode='r')
        right = 0
        wrong = 0
        predicted_data.write('Mail, Gold, Prediction, Distance')
        for line in val_data:
            self.spinner.next()
            line = line.strip().split(',')
            path = line[0]
            target = line[1]
            # namedtuple (distance, prediction)
            prediction = self.predict(path)
            predicted_data.write(path
                                 + ','
                                 + target
                                 + ','
                                 + prediction.prediction
                                 + ','
                                 + str(prediction.distance)
                                 + '\n')
            if target == prediction.prediction:
                right += 1
            else:
                wrong += 1
        total = right + wrong
        return(right, wrong, total, (right / total) * 100)

    def _find_most_common(self, train_csv):
        # computes the 200 most common nouns from
        # the subject lines of spam mails of the corpus
        # counter for all nouns found in spam subject lines
        spam_nouns_counter = Counter()
        train_file = open(train_csv, mode='r')
        for line in train_file:
            self.spinner.next()
            line = line.strip().split(',')
            path = line[0]
            target = line[1]
            if target == 'spam':
                feature_obj = Features(path)
                # nouns in subject line of single mail
                for noun in feature_obj.headline_nouns:
                    spam_nouns_counter[noun] += 1
        self.most_common_nn = set(map(lambda x: x[0],
                                  spam_nouns_counter.most_common(200)))
        train_file.close()


