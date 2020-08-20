# Hannah Peuckmann
# Matr.Nr.: 791996
# WiSe20 20.08.20
# spam classifier


import logging

from operator import add, sub

from Feature_class import Features

from collections import namedtuple

logging.basicConfig(filename='spamClassifier_log.log',level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

class SpamClassifier:
    '''  '''
    def __init__(self, extract_features=None):
        # agregated features of ham and spam
        # from file
        if extract_features != None:
                features = open(extract_features, mode='r')
                self.sum_features_spam = [float(x) for x in features.readline().split(',')[1:]]
                self.sum_features_ham =[float(x) for x in features.readline().split(',')[1:]]
        # or trained
        else:
            self.sum_features_ham = []
            self.sum_features_spam = []

    def train(self, train_csv, class_features_filename, file_features_filename):
        train_file = open(train_csv, mode='r')
        class_features = open(class_features_filename, mode='w')
        file_features = open(file_features_filename, mode='w')
        sum_features_spam = [0,0,0,0]
        sum_features_ham = [0,0,0,0]
        total_ham = 0
        total_spam = 0
        # feature extraction for each file
        for line in train_file:
            line = line.strip()
            line = line.split(',')
            path = line[0]
            target = line[1]
            feature_obj = Features(path)
            feature_obj.extract_features() ### weglassen? brauch ich net
            feature_obj.normalise_features()
            if target == 'spam':
                total_spam += 1
                # sums elements at the same index of the two lists
                sum_features_spam = list(map(add, sum_features_spam, list(feature_obj.normalised_features)))
            else:
                total_ham += 1
                sum_features_ham = list(map(add, sum_features_ham, list(feature_obj.normalised_features)))
            # write features per file to csv
            file_features.write(target
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
        # normalise class features
        self.sum_features_spam = [element/total_spam for element in sum_features_spam]
        self.sum_features_ham = [element/total_ham for element in sum_features_ham]
        # safe class features to csv
        ### geht das schöner? kürzer? bestimmt
        class_features.write('spam' + ','
                        + str(self.sum_features_spam[0]) + ','
                        + str(self.sum_features_spam[1]) + ','
                        + str(self.sum_features_spam[2]) + ','
                        + str(self.sum_features_spam[3]) + '\n'
                        )
        class_features.write('ham' + ','
                        + str(self.sum_features_ham[0]) + ','
                        + str(self.sum_features_ham[1]) + ','
                        + str(self.sum_features_ham[2]) + ','
                        + str(self.sum_features_ham[3])
                        )
        return


    def predict(self, mail):
        '''predicts class for single mail file,
           returns prediction and distance to predicted class'''
        feature_obj = Features(mail)
        mail_features = list(feature_obj.normalised_features)
        # compute distance to classes
        # difference between elements at the same index of the two feature lists
        mail_spam_dist = sum(list(map(lambda x, y: abs(x - y), mail_features, self.sum_features_spam)))
        mail_ham_dist = sum(list(map(lambda x, y: abs(x-y), mail_features, self.sum_features_ham)))
        logging.info('distance to spam class: '+ str(mail_spam_dist))
        logging.info('distance to ham class: '+ str(mail_ham_dist))
        prediction = namedtuple('prediction', 'distance prediction')
        # predict the class
        if mail_ham_dist < mail_spam_dist:
            return prediction(mail_ham_dist, 'ham')
        else:
            return prediction(mail_spam_dist, 'spam')

    def evaluate(self, val_set, predictions_file):
        predictet_data = open(predictions_file, mode='w')
        val_data = open(val_set, mode='r')
        right = 0
        wrong = 0
        total = 0
        for line in val_data:
            total += 1
            line = line.strip()
            line = line.split(',')
            path = line[0]
            target = line[1]
            prediction = self.predict(path)
            predictet_data.write(path + str(prediction.distance) + prediction.prediction + '\n')
            if target == prediction.prediction:
                right += 1
            else:
                wrong += 1
        logging.info('correct classified: '+ str(right))
        logging.info('wrong classified: ' + str(wrong))
        return(right, wrong, total, (right/total)*100)


