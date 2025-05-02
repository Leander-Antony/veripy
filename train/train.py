import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle

train_df = pd.read_csv("train_fixed.tsv", sep="\t")
test_df = pd.read_csv("test_fixed.tsv", sep="\t")


label_encoder = LabelEncoder()
train_df['label_encoded'] = label_encoder.fit_transform(train_df['label'])

vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(train_df['text'])
y = train_df['label_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))


with open("naive_bayes_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("count_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)
