# spam classifier

The project implements a binary classifier for spam and ham.
# Requirements (Ubuntu)

* Python 3.6.9

# Usage

`$ python3 main.py --data CORPUS_DIRECTORY CORPUS_SPLIT_DIRECTORY`

*CORPUS_DIRECTORY* Path to a directory that contains the six unziped files of the Enron Email Dataset.

*CORPUS_SPLIT_DIRECTORY* Directory to save the .csv-files for train, validate and test.

`$ python3 main.py --train CORPUS_CSV CLASS_FEATURE_CVS SINGLE_MAIL_FEATURE_CSV`

*CORPUS_CSV* Path to a .csv-file that contains all paths of the mails the classifier is to be trained on.

*CLASS_FEATURE_FILE* .csv-file to save the aggregated features of the two classes. 

*SINGLE_MAIL_FEATURE_FILE* .csv-file to save the features of each single mail.

`$ python3 main.py --predict CLASS_FEATURE_CSV MAIL_FILE`

*CLASS_FEATURE_CSV* Path to the .csv-file that holds the aggregated featurs that was created by --train.

*MAIL_FILE* Path to the mail a prediction should be made for. The mail needs to be a txt-file.

`$ python3 main.py --evaluate CLASS_FEATURE_CSV TEST_CORPUS_CSV PREDICTIONS.CSV`

*CLASS_FEATURE_CSV* Path to the .csv-file that holds the aggregated featurs that was created by --train.

*TEST_CORPUS_CSV* Path to a .csv-file that holds the paths of the mails that should be classified.

# Corpus

The corpus used is the [Enron Email Dataset](http://www2.aueb.gr/users/ion/data/enron-spam/)

# Creatingt the testdata

To split the corpus the mode --data can be used. Five csv-files are created, 'train.csv', 'test.csv', 'val.csv', 'all_ham.csv' und 'all_spam.csv' which holds the paths to the associated mails.

# Sample calls

`$ Python3 main.py --data Enron_spam_corpus Split_Data`

`$ Python3 main.py --train Split_Data/train.csv Data/class_features.csv Data/single_features.csv`

`$ Python3 main.py --predict Data/class_features.csv ../Enron_spam_corpus/enron1/spam/0006.2003-12-18.GP.spam.txt` 

`$ Python3 main.py --evaluate Data/class_features.csv Data/test.csv Data/predictions.csv`

  

# Author
Hannah Peuckmann
peuckmann@uni-potsdam.de
Universität Potsdam, Matriculation number 791996
