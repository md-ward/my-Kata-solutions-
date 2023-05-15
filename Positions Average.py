import re


def pos_average(s: str):
    nums = re.findall(r'[0-9]+', s)
    


print(pos_average(
    "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"))
