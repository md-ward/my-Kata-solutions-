import math
def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    if l*w*h==0:
        return numbers[0]
    else:
        return numbers[math.ceil((l * h * 2 + w * h * 2) * 1.15 / 5.2)]