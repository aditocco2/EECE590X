from logic_utils.qm2 import qm

# col = "1010000010100000" # 4 corners
col = "1010001110100011" # 4 corners and middle

ones, zeros, dc = [], [], []

for i in range(len(col)):
    if col[i] == "1":
        ones.append(i)
    elif col[i] == "0":
        zeros.append(i)
    elif col[i].lower() == "x":
        dc.append(i)

print(qm(ones, zeros, dc))