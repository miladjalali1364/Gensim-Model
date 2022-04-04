# How to Develop Word Embeddings in Python with Gensim

Word embedding algorithms like word2vec and GloVe are key to the state-of-the-art results achieved by neural network models on natural language processing problems like machine translation.

In this tutorial, you will discover how to train and load word embedding models for natural language processing applications in Python using Gensim.

# What is Word Embedding?
Word Embedding is a word representation type that allows machine learning algorithms to understand words with similar meanings.
It is a language modeling and feature learning technique to map words into vectors of real numbers using neural networks, probabilistic models, or dimension reduction on the word co-occurrence matrix.
Some word embedding models are Word2vec (Google), Glove (Stanford), and fastest (Facebook).

Word Embedding is also called as distributed semantic model or distributed represented or semantic vector space or vector space model. 
As you read these names, you come across the word semantic which means categorizing similar words together. 

For example fruits like apple, mango, banana should be placed close whereas books will be far away from these words. 

In a broader sense, word embedding will create the vector of fruits which will be placed far away from vector representation of books.

# Where is Word Embedding used?

Word embedding helps in feature generation, document clustering, text classification, and natural language processing tasks.
Let us list them.


   **Compute similar words:** 
     Word embedding is used to suggest similar words to the word being subjected to the prediction model.
   Along with that it also suggests dissimilar words, as well as most common words.

   **Create a group of related words:** 
     It is used for semantic grouping which will group things of similar characteristic together and dissimilar far away.

   **Feature for text classification:** 
     Text is mapped into arrays of vectors which is fed to the model for training as well as prediction.
   Text-based classifier models cannot be trained on the string, so this will convert the text into machine trainable form. 
   Further its features of building semantic help in text-based classification.

   **Document clustering:** 
     is another application where Word Embedding Word2vec is widely used

   **Natural language processing:** 
     There are many applications where word embedding is useful and wins over feature extraction phases such as parts of speech tagging, sentimental analysis, and syntactic analysis.
   Now we have got some knowledge of word embedding.Some light is also thrown on different models to implement word embedding. 
   This whole Word Embedding tutorial is focused on one of the models (Word2vec).



# What is Gensim?
Gensim is an open-source topic modeling and natural language processing toolkit that is implemented in Python and Cython. 
Gensim toolkit allows users to import Word2vec for topic modeling to discover hidden structure in the text body. 
Gensim provides not only an implementation of Word2vec but also for Doc2vec and FastText as well.
