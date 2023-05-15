

def find_short(string: str):
    words = string.split(' ')
    words_len = []
    for i in words:
        words_len.append (len(i))
    return min(words_len)
x="bitcoin take over the world maybe who knows perhaps"
print(find_short(x))