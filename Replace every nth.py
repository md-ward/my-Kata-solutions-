

def replace_nth(text, n, old_value, new_value):
    if n==0 or n<0:
        return text
    indices = [i for i, c in enumerate(text) if c == old_value]

    for i,j in enumerate(indices,1):
     if i%n==0:

        text = text[:indices[i-1]] + new_value + text[indices[i-1]+1:]

    return text


t = "Vader said: No, I am your father!"
print(replace_nth(t, 2, 'a', 'x'))
