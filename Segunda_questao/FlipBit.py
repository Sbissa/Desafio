def flip_bit(entry):

    k = 0xFFFFFFFF
    sizeNum = entry[0]
    entry.remove(sizeNum)
    result = []
    for x in entry:
        result.append(int(bin(x ^ k), 2))
        print(x)
    return result
