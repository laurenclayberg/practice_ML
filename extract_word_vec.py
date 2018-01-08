# currently using GloVe word vecs to practice
import sys
import re

with open(sys.argv[1], 'r') as f:
    word_vec_text = f.read()

words_to_lookup = ["man", "woman", "queen", "king"]

dictionary = {}

for word in words_to_lookup:
    regex = "\n" + word + "[ -.\d]+\n"
    dictionary[word] = re.findall(regex, word_vec_text)[0]
    dictionary[word] = re.sub("^\n", "[", dictionary[word])
    dictionary[word] = re.sub("\n", "]", dictionary[word])
    dictionary[word] = re.sub(word + " ", "", dictionary[word])
    dictionary[word] = re.sub(" ", ",", dictionary[word])
    dictionary[word] = eval(dictionary[word])

print (dictionary)
print ("Here is some vector math:")
# print (dictionary["queen"] - dictionary["woman"] + dictionary["man"] - dictionary["king"])
print ([q - w + m - k for q,w,m,k in zip(dictionary["queen"], dictionary["woman"], dictionary["man"], dictionary["king"])])
