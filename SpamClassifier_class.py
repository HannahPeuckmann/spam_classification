# spam classifier

import logging

from operator import add, sub

from Feature_class import Features

from BasicNLP_class import BasicNLP

class SpamClassifier:
    def __init__(self, spam_data, ham_data):
        self.spam_train = open(spam_data, mode='r')
        self.ham_train = open(ham_data, mode='r')
        self.ham_features = []
        self.spam_features = []

    def train(self):
        sum_features = open('Data/sum_features_extracted.csv', mode='w')
        train_feature_file = open('Data/features_extracted.csv', mode='w')
        def extract_and_safe(data, setname):
            sum_features = [0,0,0,0]
            total = 0
            for path in data:
                total += 1
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
            sum_features = [sum_features[0] / total,
                            sum_features[1] / total,
                            sum_features[2] / total,
                            sum_features[3] / total
                           ]
            return sum_features
        self.spam_features = extract_and_safe(self.spam_train, 'spam')
        self.ham_features = extract_and_safe(self.ham_train, 'ham')
        sum_features.write('spam' + ','
                        + str(self.spam_features[0]) + ','
                        + str(self.spam_features[1]) + ','
                        + str(self.spam_features[2]) + ','
                        + str(self.spam_features[3]) + '\n'
                        )
        sum_features.write('ham' + ','
                        + str(self.ham_features[0]) + ','
                        + str(self.ham_features[1]) + ','
                        + str(self.ham_features[2]) + ','
                        + str(self.ham_features[3])
                        )
        return


    def predict(self, mail):
        feature_obj = Features(mail)
        feature_obj.extract_features()
        feature_obj.normalise_features()
        mail_features = list(feature_obj.normalised_features)
        mail_spam_dist = sum(list(map(lambda x, y: abs(x - y), mail_features, self.spam_features)))
        mail_ham_dist = sum(list(map(lambda x, y: abs(x-y), mail_features, self.ham_features)))
        logging.info('distance to spam class: '+ str(mail_spam_dist))
        logging.info('distance to ham class: '+ str(mail_ham_dist))
        if mail_ham_dist < mail_spam_dist:
            return mail_ham_dist, 'ham'
        else:
            return mail_spam_dist, 'spam'

