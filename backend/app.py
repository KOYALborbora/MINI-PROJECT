from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS
import gensim.downloader as api

app = Flask(__name__)
CORS(app)

# Load the model
with open("../model.pkl", "rb") as f:
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

# Load your word embedding model
model = api.load("word2vec-google-news-300")

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def predicted_output(test):
    predictedt = []
    for j in test:
        l1 = [
            np.max([0, np.dot(j, hweights1) + hbias1]),
            np.max([0, np.dot(j, hweights2) + hbias2]),
            np.max([0, np.dot(j, hweights3) + hbias3])
        ]
        l2 = [
            np.dot(l1, weights1) + bias1,
            np.dot(l1, weights2) + bias2
        ]
        
        sftmx = softmax(l2)
        if sftmx[0] > sftmx[1]: predictedt = [1,0]
        else: predictedt = [0,1] 

    return predictedt

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    word = data.get('word')
    print(word)

    if word in model.key_to_index:
        emb = model[word][:100]  # Assuming the model gives 100-dimensional vectors
    else:
        return jsonify({'error': 'Word not found in the model'}), 400

    pred = predicted_output([emb])
    result = 'negative' if np.array_equal(pred, [1,0]) else 'positive'
    return jsonify({'word': word, 'prediction': result})


if __name__ == "__main__":
    app.run(debug=True)
