# DocumentClustering
Document clustering with stand alone Python . This is reworking of "Document clustering with Python" by  http://brandonrose.org/clustering. This version will run in a Tkinter window.  
To use nltk you have to downlad any corpus to a directory from nltk:
python -m nltk.downloader
Then link it to you code nltk.data.path.append('./nltk_data/') 
if using smoowball stemmer have to downlad the data for that from the above. In the models pick snowball_datals

"Document clustering with Python" uses sklearn fro analysis in this project I will be "rollong my own" Start with calculating TFIDF

Taken from:
http://www.tfidf.com/


Typically, the tf-idf weight is composed by two terms: the first computes the normalized Term Frequency (TF), aka. the number of times a word appears in a document, divided by the total number of words in that document; the second term is the Inverse Document Frequency (IDF), computed as the logarithm of the number of the documents in the corpus divided by the number of documents where the specific term appears.

TF: Term Frequency, which measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often divided by the document length (aka. the total number of terms in the document) as a way of normalization: 

TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).

IDF: Inverse Document Frequency, which measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scale up the rare ones, by computing the following: 

IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

See below for a simple example.

Example:

Consider a document containing 100 words wherein the word cat appears 3 times. The term frequency (i.e., tf) for cat is then (3 / 100) = 0.03. Now, assume we have 10 million documents and the word cat appears in one thousand of these. Then, the inverse document frequency (i.e., idf) is calculated as log(10,000,000 / 1,000) = 4. Thus, the Tf-idf weight is the product of these quantities: 0.03 * 4 = 0.12.



This is then used to look at differances between the documents
method used is cosine similarity informationn fom here:
https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/


Cosine Similarity (d1, d2) =  Dot product(d1, d2) / ||d1|| * ||d2||

Dot product (d1,d2) = d1[0] * d2[0] + d1[1] * d2[1] * … * d1[n] * d2[n]
||d1|| = square root(d1[0]2 + d1[1]2 + ... + d1[n]2)
||d2|| = square root(d2[0]2 + d2[1]2 + ... + d2[n]2)

note that the ||dn|| are constant for a document
