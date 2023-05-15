def add(a, b):
    return a+b


def min(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


###################################*splitby perator ###############
def splitby(string, separators):
    lis = []
    current = ""
    for ch in string:
        if ch in separators:
            lis.append(current)
            lis.append(ch)
            current = ""
        else:
            current += ch
    lis.append(current)
    return lis
# *

##################################################################! evaluation########################


def evaluation(equation: str):

    try:
        new = list(equation)
        while len(new) != 1:

            if new[0].isnumeric() and new[1].isnumeric():
                new[0] = new[0]+new[1]
                new.pop(1)

            num1 = float(new[0])
            num2 = float(new[2])
            res = ''
            if new[1] == '+':
                res = add(num1, num2)
                new[0] = str(res)
                new.pop(1)
                new.pop(1)

            elif new[1] == '-':
                res = min(num1, num2)
                new[0] = str(res)
                new.pop(1)
                new.pop(1)
            elif new[1] == '*':
                res = mul(num1, num2)
                new[0] = str(res)
                new.pop(1)
                new.pop(1)
            elif new[1] == '/':
                res = div(num1, num2)
                new[0] = str(res)
                new.pop(1)
                new.pop(1)
        return new.pop()
    except:
        return new


def calculate(equation: str):

    temp = splitby(equation, '+-')
    for i in temp:
        if '*' or '/' in i:
            temp[temp.index(i)] = evaluation(i)
    return evaluation(temp)


x = '2225*1'

print(splitby(x,'+-'))
print(calculate(x))
