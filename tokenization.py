from nltk.tokenize import word_tokenize, sent_tokenize

# Open file to read contents 
file_content = open("input.txt").read()

# tokenize the file 
tokens = word_tokenize(file_content)

# create sentences 
sentences = sent_tokenize(file_content)

print("Total words : ", len(tokens))
print("\nWords in the paragraph \n" , tokens)

print("\nTotal sentences : ", len(sentences))
print("\nSentences in the paragraph \n", sentences)