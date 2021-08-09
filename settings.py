####################***GENERAL LIB***####################
import os
import re
import pickle
import numpy as np
import pandas as pd
import json
import math
import csv
import itertools
from itertools import compress
from tqdm import tqdm
from collections import Counter
from functools import reduce
from pprint import pprint


####################***SKLEARN LIB***####################
from sklearn.preprocessing import LabelEncoder, StandardScaler # Функции для нормализации данных
from sklearn import preprocessing # Пакет предварительной обработки данных
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
from sklearn.tree import export_text



####################***TREE LIB***####################
from treelib import Node, Tree



####################***NLP LIB***####################
import spacy
from spacy.lang.ru.examples import sentences
from spacy.symbols import ORTH, LEMMA
from spacy.lang.ru import Russian
from spacy.tokens.doc import Doc
from spacy.vocab import Vocab
from spacy import displacy

# import textacy
# from textacy import extract, preprocessing

####################***NLTK LIB***####################
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer



from openpyxl import load_workbook
import pyexcel
from pyexcel._compact import OrderedDict
import xlrd, xlwt


####################***MATPLOTLIB LIB***####################
import matplotlib.pyplot as plt # Отрисовка изображений



import graphviz
from graphviz import Digraph
