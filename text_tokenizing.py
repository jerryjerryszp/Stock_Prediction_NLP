#Text Tokenizing using nltk library and Python 3

import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


#nltk.download()

#************** word and sentence tokenizing
EXAMPLE_TEXT = "Hello wadu, how are you doing today? The weather is goat, and nltk is awesome. You should be grateful."

#sentence tokenizing
print(sent_tokenize(EXAMPLE_TEXT))

#word tokenizing
print(word_tokenize(EXAMPLE_TEXT))



#************** stop words
example_sent = "This is a sample sentence, trying out the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

#************** Stemming words with NLTK
ps = PorterStemmer()

example_words = ["maybe","probably","might","possibly"]
for w in example_words:
    print(ps.stem(w))

new_text = "It is important to by very pythonly while you are pythoning with python."
words = word_tokenize(new_text)

for stems in words:
    print(ps.stem(stems))

