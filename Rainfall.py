

import re


def extract_data(town, data):
    data_split = re.findall(r'.+(?:\n|$)', data)

    towns = {}
    for i in data_split:
        temp = re.split(':', i)
        rain_vals = re.findall(r"[-+]?\d*\.?\d+|\d+", temp[1])
        rain_vals = list(map(float, rain_vals))
        towns[temp[0]] = rain_vals
    data_values = towns.get(town)
    return data_values


def mean(town, s):
    if town=='':
        return -1
    temp = extract_data(town, s)
    if temp==[]:
        return -1
    return sum(temp)/len(temp)


def variance(town, s):
    if town=='':
        return -1
    temp = extract_data(town, s)
    if temp==[]:
      return -1
    mean_temp = sum(temp)/len(temp)
    for i in temp:
        temp[temp.index(i)] = pow((i-mean_temp), 2)
    return sum(temp)/len(temp)


