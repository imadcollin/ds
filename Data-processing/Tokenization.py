#%%
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
porter_stemmer = PorterStemmer()
str = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
token = nltk.word_tokenize(str)
for w in token:
    print("Actual: %s Stem: %s" % (w, porter_stemmer.stem(w)))
    print("Actual: %s Lemma: %s" % (w, wordnet_lemmatizer.lemmatize(w)))
print(token)

sentence_token = nltk.sent_tokenize(str)
print(sentence_token)

# %%
