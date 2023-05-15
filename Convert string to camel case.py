import re


def to_camel_case(text: str):
    if text == '':
        return
    words = re.split(r'[- _]', text)
    temp = []
    for word in words:

        temp.append(word.title())
    if words[0][0].islower():
        temp[0] = words[0]

    return ''.join(temp)


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case('A_B_C'))
