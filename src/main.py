import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from model import TextGenerationLSTM

from torch.utils.data import Dataset, DataLoader
from collections import Counter
import random

# Dataset Preparation
with open('data/christmas_movies.txt', 'r', encoding='utf-8') as file:
    text = file.read()
# Tokenize the text into words
words = text.split()

with open('data/christmas_movies.txt', 'r', encoding='utf-8') as file:
    wordlist = [line.split(None, 1)[0] for line in file]
# Tokenize the text into words

random_christmas_word = random.sample(wordlist, 1)[0]

word_counts = Counter(words)
vocab = list(word_counts.keys())
vocab_size = len(vocab)
word_to_int = {word: i for i, word in enumerate(vocab)}
int_to_word = {i: word for word, i in word_to_int.items()}
SEQUENCE_LENGTH = 64
samples = [words[i:i+SEQUENCE_LENGTH+1] for i in range(len(words)-SEQUENCE_LENGTH)]
BATCH_SIZE = 32
    
    
# Training Setup
embedding_dim = 16
hidden_size = 32
num_layers = 1
learning_rate = 0.01
epochs = 50

model2 = TextGenerationLSTM(
    vocab_size, 
    embedding_dim, 
    hidden_size, 
    num_layers)
model2.load_state_dict(torch.load("output/single-word-weights.pth"))


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# Inference
def generate_text(model, start_string, num_words):
    model.eval()
    words = start_string.split()
    for _ in range(num_words):
        input_seq = torch.LongTensor([word_to_int[word] for word in words[-SEQUENCE_LENGTH:]]).unsqueeze(0).to(device)
        h, c = model.init_hidden(1)
        output, (h, c) = model(input_seq, (h, c))

        next_token_prob = torch.softmax(output, dim = -1)
        next_token_index = torch.multinomial(next_token_prob, num_samples=1)[-1].item()
        words.append(int_to_word[next_token_index])
    return " ".join(words)



generated_movie_text = generate_text(model2, start_string= random_christmas_word, num_words=60)

stripped = generated_movie_text.split(".", 1)[0] + "."
print(stripped)