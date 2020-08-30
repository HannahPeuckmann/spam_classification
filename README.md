
# Voraussetzungen (Ubuntu)

* Python 3.6.9

# Nutzung

`$ python3 main.py --data KORPUS_DIRECTORY KORPUS_SPLIT_DIRECTORY`

*KORPUS_DIRECTORY* Pfad zu einer Datei welche die sechs unziped Dateien des Enron Email Dataset enthält.

*KORPUS_SPLIT_DIRECTORY* Datei in der die .csv-Dokumente für train, validate und test gespeichert werden.

`$ python3 main.py --train KORPUS_CSV CLASS_FEATURE_CVS SINGLE_MAIL_FEATURE_CSV`

*KORPUS_CSV* Pfad zu einem .csv-Dokument welches alle Dateipfade der Mails enthält, auf denen trainiert werden soll.

*CLASS_FEATURE_FILE* .csv-Dokument in dem die aggregierten features der Klassen gespeichert werden soll. 

*SINGLE_MAIL_FEATURE_FILE* .csv-Dokument in dem die features pro Mail gespeichert werden.

`$ python3 main.py --predict CLASS_FEATURE_CSV MAIL_FILE`

*CLASS_FEATURE_FILE* Dateipfad zu der bei --train erstellten .csv-Dokument, welches die aggregierten features enthält.

*MAIL_FILE* Dateipfad einer Mail in txt Format, für die eine Vorhersage getroffen wird.

`$ python3 main.py --evaluate CLASS_FEATURE_CSV TEST_KORPUS_CSV PREDICTIONS.CSV`

*CLASS_FEATURE_CSV* Dateipfad zu der bei --train erstellten .csv-Dokument, welches die aggregierten features enthält.

*TEST_KORPUS_CSV* Dateipfad zu einem .csv-Dokument welches alle Dateipfade der Mails enthält für die der Klassififzierer evaluiert werden soll.

# Korpus

Der genutzte Korpus ist der [Enron Email Dataset](http://www2.aueb.gr/users/ion/data/enron-spam/)

# Testdaten erstellen

Zum Erstellen der Testdaten, das Aufteilen des Korpus, kann der Modus --data verwendet werden. Es werden fünf csv-Dokumente erstellt, 'train.csv', 'test.csv', 'val.csv', 'all_ham.csv' und 'all_spam.csv' welche die Dateipfade der zugehörigen Mails enthalten. 


# Beispielaufruf

`$ Python3 main.py --data Enron_spam_sorpus Split_Data`

`$ Python3 main.py --train Split_Data/train.csv Data/class_features.csv Data/single_features.csv`

`$ Python3 main.py --predict Data/class_features.csv ../Enron_spam_corpus/enron1/spam/0006.2003-12-18.GP.spam.txt` 

`$ Python3 main.py --evaluate Data/class_features.csv Data/test.csv Data/predictions.csv`

  

# Autorin
Hannah Peuckmann
peuckmann@uni-potsdam.de
Universität Potsdam, Matrikelnummer 791996
