

def wave(people):

    temp = []
    for i in range(len(people)):
        if people[i] == ' ':
            continue

        else:
            x = people[:i]+people[i].upper()+people[i+1:]
            temp.append(x)
    return temp
###########test case########


a = wave('two words')
print(a)

b = ['Two words', 'tWo words', 'twO words', 'two Words',
     'two wOrds', 'two woRds', 'two worDs', 'two wordS']


print(len(a), len(b))
for i in range(len(a)):
    print(a[i] == b[i])
##########################################
