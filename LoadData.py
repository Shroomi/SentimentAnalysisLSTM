import numpy as np

###################### load word list and word vectors from GloVe ##########################
wordsList = np.load('wordsList.npy')
print('Successfully loaded the word list!')
#print(type(wordsList)) # Originally, the type of wordsList is numpy
wordsList = wordsList.tolist()
wordsList = [word.decode('UTF-8') for word in wordsList]
wordVectors = np.load('wordVectors.npy')
print('Successfully loaded the word vectors!')

print(type(wordVectors))
print('The number of words: ' + str(len(wordsList)))
print('The shape of word vectors: ' + str(wordVectors.shape))
################################# test embedding matrix #####################################
# baseballIndex = wordsList.index('baseball')
# print(wordVectors[baseballIndex])
###################### load word list and word vectors from GloVe ##########################