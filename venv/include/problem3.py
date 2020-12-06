## Sentence -> Input, Key -> word ,Value ->length of the word

sentence = input("Enter the Sentence")
words = sentence.split(" ")
# print(words)    for exaple
count_words = {word:len(word) for word in words}
print(count_words)
