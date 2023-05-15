from collections import Counter

def scramble(s1,s2):
    counter1 = Counter(s1)
    counter1.subtract(Counter(s2))
    return (all(e >= 0 for e in counter1.values()))





print(scramble('hello worslld', 'hello world'))
print( scramble('rkqodlw', 'world'))  # True
print(scramble('cedewaraaossoqqyt', 'codewars')) # True
print(scramble('katas', 'steak')) #False
