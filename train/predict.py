import pickle

# Load all components
with open('naive_bayes_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('count_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

with open('label_encoder.pkl', 'rb') as label_file:
    label_encoder = pickle.load(label_file)

# Function to predict the label of new text
def predict_label(text):
    # Preprocess and vectorize
    vectorized = vectorizer.transform([text])
    
    # Predict
    prediction = model.predict(vectorized)
    
    # Decode label
    predicted_label = label_encoder.inverse_transform(prediction)[0]
    return predicted_label

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a statement to classify: ")
    result = predict_label(user_input)
    print(f"\nPredicted Label: {result}")
