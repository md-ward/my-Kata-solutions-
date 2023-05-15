def uncensor(infected, discovered):

    newText = ''
    count = -1
    for i in infected:
        if i == '*':
            count += 1
            newText += discovered[count]

        else:
            newText += i
    return newText


print(uncensor('s*das*das*das*d','1114'))
