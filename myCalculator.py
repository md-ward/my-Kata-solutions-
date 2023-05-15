import tkinter as tk

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
        return new[0]


def calculate(equation: str):

    temp = splitby(equation, '+-')
    for i in temp:
        if '*' or '/' in i:
            temp[temp.index(i)] = evaluation(i)
    return evaluation(temp)
calculations = ''


def add_to_calculation(symbol):
    global calculations
    calculations += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculations)


def evaluate_calculation():
    global calculations
    try:
        print(calculate(calculations))
        result = str(  calculate(calculations))
        print(result)

        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)

    except:
        clear_field()
        text_result.insert(1.0, 'error')


def clear_field():
    global calculations
    calculations = ''
    text_result.delete(1.0, 'end')


root = tk.Tk()
root.geometry('300x350')
text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)
bt1 = tk.Button(root, text='1', command=lambda: add_to_calculation(
    1), width=5, font=('Arial', 15))
bt1.grid(row=2, column=1)


bt2 = tk.Button(root, text='2', command=lambda: add_to_calculation(
    2), width=5, font=('Arial', 15))
bt2.grid(row=2, column=2)
bt3 = tk.Button(root, text='3', command=lambda: add_to_calculation(
    3), width=5, font=('Arial', 15))
bt3.grid(row=2, column=3)

bt4 = tk.Button(root, text='4', command=lambda: add_to_calculation(
    4), width=5, font=('Arial', 15))
bt4.grid(row=3, column=1)
bt5 = tk.Button(root, text='5', command=lambda: add_to_calculation(
    5), width=5, font=('Arial', 15))
bt5.grid(row=3, column=2)
bt6 = tk.Button(root, text='6', command=lambda: add_to_calculation(
    6), width=5, font=('Arial', 15))
bt6.grid(row=3, column=3)
bt7 = tk.Button(root, text='7', command=lambda: add_to_calculation(
    7), width=5, font=('Arial', 15))
bt7.grid(row=4, column=1)
bt8 = tk.Button(root, text='8', command=lambda: add_to_calculation(
    8), width=5, font=('Arial', 15))
bt8.grid(row=4, column=2)
bt9 = tk.Button(root, text='9', command=lambda: add_to_calculation(
    9), width=5, font=('Arial', 15))
bt9.grid(row=4, column=3)
bt0 = tk.Button(root, text='0', command=lambda: add_to_calculation(
    0), width=5, font=('Arial', 15))
bt0.grid(row=5, column=1)

bt_left = tk.Button(root, text='(', command=lambda: add_to_calculation(
    '('), width=5, font=('Arial', 15))
bt_left.grid(row=5, column=2)

bt_right = tk.Button(root, text=')', command=lambda: add_to_calculation(
    ')'), width=5, font=('Arial', 15))
bt_right.grid(row=5, column=3)

bt_plus = tk.Button(
    root, text='+', command=lambda: add_to_calculation('+'), width=5, font=('Arial', 15))
bt_plus.grid(row=6, column=1)
bt_min = tk.Button(
    root, text='-', command=lambda: add_to_calculation('-'), width=5, font=('Arial', 15))
bt_min.grid(row=6, column=2)
bt_mul = tk.Button(
    root, text='*', command=lambda: add_to_calculation('*'), width=5, font=('Arial', 15))
bt_mul.grid(row=6, column=3)
bt_div = tk.Button(
    root, text='/', command=lambda: add_to_calculation('/'), width=5, font=('Arial', 15))
bt_div.grid(row=7, column=1)

bt_eq = tk.Button(root, text='=', command= lambda: evaluate_calculation(),
                  width=5, font=('Arial', 15))
bt_eq.grid(row=7, column=2)
bt_clear = tk.Button(
    root, text='C', command=lambda: clear_field(), width=5, font=('Arial', 15))
bt_clear.grid(row=7, column=3)


root.mainloop()
