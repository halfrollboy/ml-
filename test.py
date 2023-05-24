import csv
import re
import numpy as np

# with open("message_new", "a") as file_message:
#     reader = csv.reader(file_message)


dic = {}
mass = []

with open("yo/labels_copy.csv", "r") as file_label:
    reader = csv.reader(file_label)
    for row in reader:
        dic[row[0]] = row[1]


with open("yo/messages_copy_new.csv", "r") as file_messages:
    reader = csv.reader(file_messages)
    for row in reader:
        # print(row[3])
        reg = re.compile("[^a-zA-Z|а-яА-Я]")
        row[3] = reg.sub(" ", row[3]).lower()
        row[3] = re.sub(" +", " ", row[3])
        mass.append(row)
print(mass[0])
mas = mass[1:]
np.random.shuffle(mas)
print(mass[0])


with open("labels.csv", "w") as labels_file:
    writer_l = csv.writer(labels_file)
    writer_l.writerow(["id", "label"])
    with open("messages.csv", "w") as messages_file:
        writer_w = csv.writer(messages_file)
        writer_w.writerow(["id", "source_message_id", "source", "text"])
        for row in mas:
            writer_l.writerow([row[0], dic[row[0]]])
            writer_w.writerow(row)
