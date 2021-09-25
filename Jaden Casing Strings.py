def to_jaden_case(string):
    z=string.split(" ")
    a=""
    for i in z:
       a+=i.capitalize()+" "
    return a[0:len(a)-1]    