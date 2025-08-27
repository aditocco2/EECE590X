def string_to_som(string):
    minterms = []
    for i in range(8):
        if string[i] == '1':
            minterms.append(f"{i}")
    minterms = " + ".join(minterms)
    return minterms
