# import nltk
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer

# train_text = state_union.raw("./2005-GWBush.txt")
# sample_text = state_union.raw("./2006-GWBush.txt")

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# tokenized = custom_sent_tokenizer.tokenize(sample_text)

# def process_content():
#     try:
#         for i in tokenized[5:]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             namedEnt = nltk.ne_chunk(tagged, binary=True)
#             namedEnt.draw()
#     except Exception as e:
#         print(str(e))


# process_content()



import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]
print(word_features)