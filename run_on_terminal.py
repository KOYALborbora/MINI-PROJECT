import streamlit as st
import pandas as pd
import numpy as np
import pickle
import gensim.downloader as api

with open("model.pkl", "rb") as f:
    model_data = pickle.load(f)

hweights1 = model_data["hweights1"]
hweights2 = model_data["hweights2"]
hweights3 = model_data["hweights3"]
hbias1 = model_data["hbias1"]
hbias2 = model_data["hbias2"]
hbias3 = model_data["hbias3"]
weights1 = model_data["weights1"]
weights2 = model_data["weights2"]
bias1 = model_data["bias1"]
bias2 = model_data["bias2"]

print("Loading word file...")
# Load your word embedding model
model = api.load("word2vec-google-news-300")
print("Word file loaded successfully...")

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0)

def predicted_output(emb):
    predictedt = []
    l1 = [
            np.max([0, np.dot(emb, hweights1) + hbias1]),
            np.max([0, np.dot(emb, hweights2) + hbias2]),
            np.max([0, np.dot(emb, hweights3) + hbias3])
        ]
    l2 = [
        np.dot(l1, weights1) + bias1,
        np.dot(l1, weights2) + bias2
    ]
        
    sftmx = softmax(l2)
    predicted = []
    if sftmx[0] > sftmx[1]: 
        predicted = [1,0]
    else:
        predicted = [0,1]
        
    return predicted

# Function to predict if a word is positive or negative
def predict(word):
    emb = []
    if word in model.key_to_index:
        emb = model[word][:100]  # Extract the first 5 dimensions of the word embedding
    else:
        return None

    pred = predicted_output(emb)
    if np.array_equal(pred, [1,0]):
        return "negative"
    else:
        return "positive"

ans = ""

while ans != "n":
    s = input("Enter word to check for: ")
    pr = predict(s)
    print(f'The word {s} is {pr}')
    ans = input("Enter more(y/n): ")
