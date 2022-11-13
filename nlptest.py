import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# EXAMPLE_TEXT = open(r'C:/Users/vadapala/Desktop/data.txt','r').read()
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard. i want to open a bank account. i want to go to America"

# Data preprocessing/cleaning
cleaneddata = re.sub(r'[.,!?]','',EXAMPLE_TEXT)

# print(cleaneddata)

stop_word = stopwords.words('english')
stop_word.extend(['the','The','THE','.',',','!','n\'t'])

# print(stop_word,'\n')

tokens = word_tokenize(cleaneddata)

cleanedtokens = []

for token in tokens:
	if token.casefold() not in stop_word:
		cleanedtokens.append(token)


stemmer = PorterStemmer()

# for t in cleanedtokens:
# 	print(stemmer.stem(t))

stemed_tokens = [stemmer.stem(cleanedtoken) for cleanedtoken in cleanedtokens]
# print(stemed_tokens)


postaggedlist = nltk.pos_tag(stemed_tokens)
# print(postaggedlist)

# Chunking:
# chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""  # RB-adverb	very, silently,VB-verb, base form take, 
# chunkParser = nltk.RegexpParser(chunkGram)     # NNP-proper noun, singular 'Harrison', NN-noun, singular 'desk',NNS-noun plural	'desks'
# chunked = nltk.RegexpParser(r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}""").parse(postaggedlist)
# print(chunked)
# chunked.draw()

# for subtree in chunked.subtrees():
#     subtree.draw()

# for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
# 	print(subtree)

# Chinking:

# chinked = nltk.RegexpParser(r"""Chunk: {<.*>+}
# 	}<VB.?|IN|DT|TO>+{""").parse(postaggedlist)
# chinked.draw()

# Entity

namedEnt = nltk.ne_chunk(postaggedlist, binary=False)
namedEnt.draw()

# print([nltk.stem.WordNetLemmatizer.lemmatize(y) for y in stemed_tokens])
# print(nltk.stem.WordNetLemmatizer.lemmatize('goig'))

# from nltk.stem import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("geese"))