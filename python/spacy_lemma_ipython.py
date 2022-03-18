# run this on Jupyter Notebooks or Google Colab

!pip install -U spacy
!python -m spacy download it_core_news_sm
import spacy

# restart the runtime

import spacy

nlp = spacy.load('it_core_news_sm')
doc = nlp('le ragazze fecero')
print(" ".join(token.lemma_ for token in doc))

# result: "il ragazza fare"
# this is called "stemmatization"
