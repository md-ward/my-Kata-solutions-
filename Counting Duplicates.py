from typing import Counter


def duplicate_count(text: str):
    temp = Counter(text.lower())
    duplicates=0
    for char, count in temp.items():
        if count>=2:
            duplicates+=1
            print(char,count)
    return temp,'Duplicates ={}'.format(duplicates)


print(duplicate_count("ABBA"))
