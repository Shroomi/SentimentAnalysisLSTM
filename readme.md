<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Sentiment Analysis with LSTMs in Tensorflow
## Load Word List and Word Vectors from GloVe
- Download `_glove.6B.zip_` to get word vectors of 400,000 vocabularies with 50 dimensions from [GloVe](https://nlp.stanford.edu/projects/glove/).
- In `LoadData.py`, we can get word list consists of 400,000 words named `wordsList`, and 400,000$$\times$$50 dimensional embedding matrix named `wordVectors`.