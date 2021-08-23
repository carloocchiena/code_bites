import string
text = "today is a beautiful day, i like this day! today."
text = text.translate(str.maketrans("", "", string.punctuation)).lower()
words = text.split()
test = dict()
for word in words:
    test[word] = test.get(word,0) + 1
