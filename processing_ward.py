import pandas as pd
import nltk
import re
import csv
from stop_words import get_stop_words
from nltk.stem.snowball import SnowballStemmer
#nltk.download('punkt')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy import cluster
import numpy as np
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt


en_stop = get_stop_words('en')
text = open('missions_un_consultive.txt', 'r')
reader = csv.reader(text, delimiter = '\t')
doc_set = []
orgs = []

for row in reader:
    orgs.append(row[0].strip())
    doc_set.append(row[0].strip() + " " + row[1])

stopwords = get_stop_words('en')
stemmer = SnowballStemmer("english")

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens


totalvocab_stemmed = []
totalvocab_tokenized = []
for i in doc_set:
    allwords_stemmed = tokenize_and_stem(i)  # for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed)  # extend the 'totalvocab_stemmed' list
    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')

tfidf_vectorizer = TfidfVectorizer(max_df=0.6, max_features=200000,
                                 min_df=0.3, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

tfidf_matrix = tfidf_vectorizer.fit_transform(doc_set) #fit the vectorizer to synopses
terms = tfidf_vectorizer.get_feature_names()
dist = 1 - cosine_similarity(tfidf_matrix)


linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances

fig, ax = plt.subplots(figsize=(80, 65)) # set size
ax = dendrogram(linkage_matrix, orientation="top", labels=orgs,
                truncate_mode="level", p=35, color_threshold=21,
                leaf_font_size=16);

groups = cluster.hierarchy.cut_tree(linkage_matrix, height=21)
groups = [group[0] for group in groups]
label_colors = {}
for i in range(0, len(orgs)):
    org = orgs[i]
    group = groups[i]
    if group == 0:
        col = 'g'
    elif group == 1:
        col = 'y'
    elif group == 2:
        col = 'b'
    elif group == 3:
        col = 'r'
    elif group == 4:
        col = 'm'
    elif group == 5:
        col = 'g'
    elif group == 6:
        col = 'k'
    label_colors[org] = col

ax = plt.gca()

xlbls = ax.get_xmajorticklabels()
for lbl in xlbls:
    lbl.set_color(label_colors[lbl.get_text()])

plt.tight_layout()
plt.savefig('ward_clusters.png', dpi=200) #save figure as ward_clusters


cutree = cluster.hierarchy.cut_tree(linkage_matrix, n_clusters = [3, 5, 10, 15])


cutree = cluster.hierarchy.cut_tree(linkage_matrix, height=50)


def find_salient_words(defined_corpus, top_n = 5):
    # defined_corpus should be format
    # [ [[text1], [text2], ... [textn]] , [1, 2, ... n] ]

    tokenizer = RegexpTokenizer(r'\w+')

    text = defined_corpus[0]
    text = [tokenizer.tokenize(i.lower()) for i in text]
    text = [[j for j in i if len(j) > 4] for i in text]
    text = [i for i in text if not i in en_stop]

    classifications = defined_corpus[1]
    top = []
    names = []
    for c in list(set(classifications)):
        indices = [i for i, x in enumerate(classifications) if x == c]
        index_text = [text[i] for i in indices]
        unique = [list(set(i)) for i in index_text]
        unique = Counter([item for sublist in unique for item in sublist])
        index_text = [[j for j in i if unique[j] > 4] for i in index_text]
        index_text = [" ".join(i) for i in index_text]

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(index_text)
        indices = np.argsort(vectorizer.idf_)[::-1]
        features = vectorizer.get_feature_names()
        top_features = [features[i] for i in indices[:top_n]]
        top.append(top_features)

        #rel_orgs = [orgs[i] for i in indices]
        #names.append(rel_orgs[:2])
    return top


def get_group(name, orgs, list):
    i = orgs.index(name)
    return list[i]

h = 19
cutree = cluster.hierarchy.cut_tree(linkage_matrix, height=h)
cutree = [i[0] for i in cutree]
find_salient_words([doc_set, cutree], top_n = 7)