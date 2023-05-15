import re


def spin_words(sentence: str):
    words = sentence.split()
    for word in words:
        if word.__len__() >= 5:

            words[words.index(word)] = ''.join(reversed(word))

    return ' '.join(words)


print(spin_words("Hey fellow warriors"))  # returns "Hey wollef sroirraw"
print(spin_words("This is a test"))  # returns "This is a test"
print(spin_words("This is another test"))  # returns "This is rehtona test"
