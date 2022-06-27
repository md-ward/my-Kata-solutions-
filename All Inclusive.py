

def getAllRotations(str):
    all_rot = []
    lenn = len(str)

    # Generate all rotations
    # one by one and print
    temp = [0] * (lenn)
    for i in range(lenn):
        j = i  # Current index in str
        k = 0  # Current index in temp

        # Copying the second part from
        # the point of rotation.
        while (j < len(str)):

            temp[k] = str[j]
            k += 1
            j += 1

        # Copying the first part from
        # the point of rotation.
        j = 0
        while (j < i):

            temp[k] = str[j]
            j += 1
            k += 1
        all_rot.append(''.join(temp))
    return all_rot    

def contain_all_rots(strng, arr):
    if strng == '':
        return True
    temp = getAllRotations(strng)
    check = all(item in arr for item in temp)

    if check:
        return True
    else :return False


print(
    contain_all_rots(
        "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))
