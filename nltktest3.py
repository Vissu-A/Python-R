import nltk
import re 
rawdata = open(r'C:/Users/vadapala/Desktop/data3.txt','r').read()
cleaneddata = re.sub(r'[.,!?]','',rawdata)
stop_word = nltk.corpus.stopwords.words('english')
stop_word.extend(['the','The','THE','.',',','!','n\'t'])
tokens = nltk.word_tokenize(cleaneddata)
cleanedtokens = []

for token in tokens:
	if token.casefold() not in stop_word:
		cleanedtokens.append(token)
print(cleanedtokens)
