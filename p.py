from keras.layers import Embedding, SimpleRNN
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


# feature_extraction = TfidfVectorizer()
# X = feature_extraction.fit_transform(messages["text"].values)

# num_training = 2813
# input_train = X[:6000]
# input_test = X[6000:]
# y_train = labels["label"].values[:6000]
# y_test = labels["label"].values[6000:]

# model = Sequential()
# model.add(Embedding(10000, 32))
# model.add(LSTM(32))
# model.add(Dense(1, activation="sigmoid"))
# model.compile(optimizer="rmsprop", loss="binary_crossentripy", metrics=["acc"])
# history = model.fit(
#     input_train, y_train, epochs=10, batch_size=128, validation_split=0.2
# )
