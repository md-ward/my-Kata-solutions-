def add_letters(*letters):
    if len(letters) == 0:
        return 'z'
    else:
        sum = 0
        for i in letters:
            sum += ord(i) - 96

        while sum > ord('z') - 96:
             sum -= ord('z') - 96

        return chr(sum + 96)
