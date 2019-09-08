#stemming is the morphological variants of same root word
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

#words to be stemmed (list)
stem_words = ["eat", "eats", "eating", "eaten", "eater", "received","receiving"]

#find stem word for each of the word in the list
for word in stem_words:
    print(word, " : ",ps.stem(word))

#stemming a sentence 
'''
    1. tokennize each word
    2. find stem word or each word
'''    
file_content = open("input.txt").read()
tokens = word_tokenize(file_content)

for word in tokens:
    print(word ," : ", ps.stem(word))