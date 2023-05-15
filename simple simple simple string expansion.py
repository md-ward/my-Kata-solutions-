import re


def string_expansion(s):
    data = re.findall(r'[0-9]*[a-zA-Z]*', s)
    print(data)
    temp = []
    for i in data:

      nums = re.findall(r'[0-9]', i)
      chars = re.findall(r'[a-zA-Z]', i)
      if nums.__len__()==0 and chars.__len__()!=0:
                temp.append(i)
                continue
      if chars.__len__()==0:
                continue  
      temp.append(string_expansion_for_one_str(i))
    return ''.join(temp)


def string_expansion_for_one_str(s):

    data = re.findall(r'[0-9][a-zA-Z]*', s)
    result = []
    
    print(data)
    if data.__len__() == 1:

        temp = re.findall(r'[a-zA-Z]', data[0])
        num = data[0][0]
        for i in temp:
            res = i*int(num)
            result.append(res)

    else:

        for val in data:

            if len(val) != 2:
                continue
            num = val[0]
            char = val[1]
            result.append(int(num)*char)

    return ''.join(result)



print(string_expansion('5919nf3u'))
