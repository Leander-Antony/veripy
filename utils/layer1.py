import pickle

with open('model/naive_bayes_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('model/count_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

with open('model/label_encoder.pkl', 'rb') as label_file:
    label_encoder = pickle.load(label_file)

def predict_label(text):

    vectorized = vectorizer.transform([text])

    prediction = model.predict(vectorized)

    predicted_label = label_encoder.inverse_transform(prediction)[0]
    return predicted_label

if __name__ == "__main__":
    user_input = input("Enter a statement to classify: ")
    result = predict_label(user_input)
    print(f"\nPredicted Label: {result}")
