from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
import string
import csv

text = open('C:\\Users\\Salena\\Documents\\clusteringEthics\\missions_dukedata.txt', 'r')
reader = csv.reader(text, delimiter = '\t')
doc_set = []
p_stemmer = PorterStemmer()
en_stop = get_stop_words('en')
tokenizer = RegexpTokenizer(r'\w+')

for row in reader:
    doc_set.append(row[1])

texts = []

for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stopped_tokens)

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics = 4, num_words = 4))