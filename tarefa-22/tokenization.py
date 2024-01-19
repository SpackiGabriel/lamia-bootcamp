from keras.preprocessing.text import Tokenizer

sentences = [
    'i love my dog',
    'i love my cat'
]

tokenizer = Tokenizer(num_words=100)

tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

print(word_index)
print(sequences)