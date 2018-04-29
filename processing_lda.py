from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
import string
import csv

text = open('missions_dukedata.txt', 'r')
reader = csv.reader(text, delimiter = '\t')
doc_set = []
organizations = []
p_stemmer = PorterStemmer()
en_stop = get_stop_words('en')
tokenizer = RegexpTokenizer(r'\w+')

for row in reader:
    organizations.append(row[0])
    doc_set.append(row[1])

texts = []

for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stopped_tokens = [i for i in stopped_tokens if len(i) > 3]
    #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stopped_tokens)

unique = [list(set(i)) for i in texts]
unique = [item for sublist in unique for item in sublist]

texts = [[j for j in i if (unique.count(j) < 70 and unique.count(j) > 5)] for i in texts]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
num = 20
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=num, id2word = dictionary)
print(ldamodel.print_topics(num_topics=num, num_words = 8))