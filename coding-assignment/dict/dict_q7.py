#Count Words in a Sentence
#Question: Write a program that counts the occurrences of each word in a given sentence and stores them in a dictionary.

#Solution:
sentence = "this is a test this is only a test"
word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count) # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
