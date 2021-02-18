import pandas as pd  # For data handling
from time import time  # To time our operations
from collections import defaultdict  # For word frequency
import re
import numpy as np

import spacy  # For preprocessing

import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
'''
Collect the dictionary of companies and assign the extracted vocabulary 
(weight vectors) to each name ???
Decision tree with bigrams collocations ???
Jaccard Distance & Q-grams

TODO
1. Normalized tokens
2. Learn cooccurrence
3. Guess the allocation 
'''

df = pd.read_csv('data/reference_dict.csv')

def mapping(tokens):
    word_to_id = dict()
    id_to_word = dict()

    for i,token in enumerate(set(tokens)):
        word_to_id[token] = i
        id_to_word[i] = token

    return word_to_id,id_to_word

def gen_training_data(tokens, word_to_id, window_size):
    N = len(tokens)
    X,Y = [],[]

    for i in range(N):
        nrb_inds = list(range(max(0, i -window_size)) +
                        list(range(i + 1, min(N, i + window_size + 1))))
        for j in nrb_inds:
            X.append(word_to_id[tokens[i]])
            Y.append(word_to_id[tokens[j]])

    X = np.array(X)
    X = np.expand_dims(X, axis=0)
    Y = np.array(Y)
    Y = np.expand_dims(Y, axis=0)

    return X, Y

nlp = spacy.load('de_core_news_sm', disable=['ner', 'parser']) # disable NER parser for speed

t = time()
data = (name.lower() for name in df['Used_name'])
df_clean = 'Abfallwirtschaftsbetrieb München'\
           'Amt für Abfallwirtschaft'\
           'AWM Abfallwirtschaftsbetrieb München'\
           'AWM/AN/SSM'\
           'Abfall wirtschaft betrieb muenchen'\
           'Dr. Pfanner GmbH'\
           'IQ GmbH' '2-Rent Group GmbH'\
           '4C GROUP AG' 'A&U Gerüstbau'\
           'Kosik'\
           'ISO inside-out-media e.K.'\
           'A. Redl GmbH'\
           'Elektromaschinen A. Redl GmbH'\
           'a/fpw - agenturfürplakatwerbung'\
           'a+p Architekten'\
           'ABB AG'\
           'ABB AG EPDS-SF'\
           'Abel GmbH'\
           'Abel Mobilfunk GmbH & Co. KG'\
           'Abendverkauf Gulin'\
           'Abendzeitung (nicht verwenden)'

# txt = [doc for doc in nlp.pipe(data, batch_size = 5000, n_threads=1)]

# df_clean = pd.DataFrame({'clean': txt})
word_to_id, id_to_word = mapping(df_clean)
X,Y = gen_training_data(df_clean, word_to_id, 3)
vocab_size = len(id_to_word)
m=Y.shape
Y_one_hot = np.zeros((vocab_size,m))
Y_one_hot[Y.flatten(), np.arrange(m)] = 1