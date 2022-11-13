import nltk
# from nltk.book import text4

stop_words =  set(stopwords(english))

msg = input('enter your text here')

tokens  = nltk.word_tokenize(msg)

print(tokens)

print([nltk.pos_tag(token.lower()) for token in tokens])