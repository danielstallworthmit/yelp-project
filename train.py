# get the yelp data from https://github.com/vc1492a/Yelp-Challenge-Dataset/blob/master/Prepped%20Data/output.csv?raw=true

import wandb
from wandb.wandb_keras import WandbKerasCallback

from keras.layers import Embedding, LSTM, Dense, Conv1D, MaxPooling1D, Dropout, Activation
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import np_utils

import pandas as pd

run = wandb.init()
config = run.config
summary = run.summary

df = pd.read_csv('yelp.csv')

text = df['text']
target = df['sentiment']

print(text[0])



