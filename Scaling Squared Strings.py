def scale(strng, k, v):
    # your code

    words = strng.split('\n')
    splitedWords = []
    tempWord = ''
    result = ''
    for word in words:
        for i in word:
            tempWord += i*k

        splitedWords.append(tempWord)

        result += (tempWord+'\n')*v
        tempWord = ''
    return result.strip('\n')


print(scale("abcd\nefgh\nijkl\nmnop", 2, 3))
