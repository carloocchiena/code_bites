# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:54:37 2019
Introduction to machine learning
https://www.codementor.io/garethdwyer/introduction-to-machine-learning-with-python-and-repl-it-rln7ywkhc?utm_swu=6096
@author: Carlo
"""
from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer

OK_txt = ["ti voglio bene", "ti amo molto", "mi piace tanto", "molto bello"] 
        
NOK_txt = ["ti odio", "ti odiamo", "non mi capisce", "non lo sopporto"]

TST_txt = ["ti odio molto", "noi ci amiamo", "non mi capisce", "è molto bello"]

training_txt = OK_txt + NOK_txt        
        
training_labels = ["positive"] * len(OK_txt) + ["negative"] * len(NOK_txt)         

print (training_labels)

vectorizer = CountVectorizer()

vectorizer.fit(training_txt)

print(vectorizer.vocabulary_)

training_vectors = vectorizer.transform(training_txt)
testing_vectors = vectorizer.transform(TST_txt)

classifier = tree.DecisionTreeClassifier()
classifier.fit(training_vectors, training_labels)
predictions= classifier.predict(testing_vectors)
print(predictions)

tree.export_graphviz(classifier, out_file="tree.dot",feature_names=vectorizer.get_feature_names(),)

def manual_classify (text):
    if "odio" in text:
        return "negative"
    if "non" in text:
        return "negative"
    return "positive"

predictions = []

for text in TST_txt:
    prediction = manual_classify(text)
    predictions.append(prediction)
print(predictions)

