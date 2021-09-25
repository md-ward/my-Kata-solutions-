def get_section_id(scroll, sizes):
    totalsize=0
    for i, num in enumerate(sizes):
        totalsize += num
        if totalsize > scroll:
            return i 
    return -1
    