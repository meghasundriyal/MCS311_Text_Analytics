from nltk import word_tokenize, pos_tag

'''
 POS(Parts of Speech) tagging associates a POS tag with each token
 Steps involved: 
  1. tokenize
  2. assign tags
'''

#open file to read its contents
file_content = open("input.txt").read()

#tokenize it
tokens = word_tokenize(file_content)

#tag each tooken 
tags = pos_tag(tokens)

print(tags)