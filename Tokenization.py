#%%
import nltk

str = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
token = nltk.word_tokenize(str)
print(token)

sentence_token = nltk.sent_tokenize(str)
print(sentence_token)
# %%
