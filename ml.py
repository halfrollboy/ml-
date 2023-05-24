# # TF-IDF
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer

# train, test = train_test_split(data, random_state=42, test_size=0.30, shuffle=True)


# vectorizer = TfidfVectorizer(strip_accents='unicode', analyzer='word', ngram_range=(1,3), norm='l2')
# vectorizer.fit(train_text)
# vectorizer.fit(test_text)x_train = vectorizer.transform(train_text)
# y_train = train.drop(labels = ['id','comment_text'], axis=1)x_test = vectorizer.transform(test_text)
# y_test = test.drop(labels = ['id','comment_text'], axis=1)
import csv
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import SVC
import pandas as pd

mass = []
# df = pd.read_csv("messages.csv", encoding="utf-8")
# df = df[["id", "text"]]
# df.head()
# mass_message = []
# mass_labels = []
labels = {}

with open("labels.csv", "r", encoding="utf-8") as file_labels1:
    reader_l1 = csv.reader(file_labels1)
    for row in reader_l1:
        labels[row[0]] = row[1]


dic = {"other": 0, "event": 0, "task": 0}
with open("messages.csv", "r", encoding="utf-8") as file_message:
    reader_m = csv.reader(file_message)
    for row in reader_m:
        mass.append()


events = []
tasks = []


with open("items.csv", "w") as item_file:
    writer_messages = csv.writer(item_file)
    writer_messages.writerow(["id", "text", "label"])
    for i in mass:


# with open("tasks.csv", "r", encoding="utf-8") as file_labels2:
#     reader_l2 = csv.reader(file_labels2)
#     for row in reader_l2:
#         item = " ".join(row)
#         tasks.append(item)

# with open("messages.csv", "w") as labels_file:
#     writer_messages = csv.writer(labels_file)
#     with open("labels.csv", "w") as labels_file:
#         writer_l = csv.writer(labels_file)
#         ids = 8500
#         for task in tasks:
#             ids = ids + 1
#             writer_messages.writerow([ids, "1154371210-37003", "chatgpt", task])
#             writer_l.writerow([ids, "task"])

#         for event in events:
#             print(event)
#             ids = ids + 1
#             writer_messages.writerow([ids, "1154371210-37003", "chatgpt", event])
#             writer_l.writerow([ids, "event"])

# with open("labels.csv", "r", encoding="utf-8") as file_labels:
#     reader_l = csv.reader(file_labels)
#     d = {"id": 0, "task": 0, "event": 0, "other": 0, "label": 0}
#     for row in reader_l:
#         d[row[1]] = d[row[1]] + 1
#     print(d)
# размешиваем данные
# np.random.shuffle(mass_words)

# print(mass_words)
# feature_extraction = TfidfVectorizer()
# X = feature_extraction.fit_transform(data["combined_news"].values)
