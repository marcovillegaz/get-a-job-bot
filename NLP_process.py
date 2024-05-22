# In this script, the job description stored in text file is been analysed using
# Natural Language Processing (NLP) techniques
import spacy
from spacy import displacy

# Create space instance
nlp = spacy.load("es_core_news_sm")
""" ner = nlp.get_pipe("ner")
print(ner.labels) """

# open text file
with open("data\Job1.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Define doc
doc = nlp(text)

""" # Print tokens
print("Tokens".center(50, "-"))
for token in doc[:10]:
    print(token) """

# print sentences
print("Sentences".center(50, "-"))
for i, sent in enumerate(doc.sents):
    print(i, sent)

""" # print entinties
print("Entities".center(50, "-"))
for ent in doc.ents:
    print(ent.text, ent.label_) """


sentence1 = list(doc.sents)[9]
print(sentence1)
for token in sentence1:
    print(token, token.dep_)

displacy.serve(sentence1, style="dep")
