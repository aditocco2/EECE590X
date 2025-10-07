from TruthTableHTML.html_tt import html_tt
import json

with open("fsm_2.txt", "r") as f:
    fsm_2 = json.load(f)

# fsm_2 = json.dumps(fsm_2, indent=4)
print(fsm_2)

# To do: somehow convert FSM JSON data to state table columns

# q1q0a q1+ q0+ F
# 000   0   0   0
# 001   0   1   0   
# 010   0   1   0
# 011   1   0   0 
# 100   0   0   1
# 101   0   0   1
# 110   x   x   x
# 111   x   x   x
Q1p = "000100xx"
Q0p = "011000xx"
F   = "000011xx" 

out_cols = [Q1p, Q0p, F]
headers = ["Q1", "Q0", "a", "Q1+", "Q0+", "F"]

html_output = html_tt(out_cols, headers)

with open("state_table.html", "w") as f:
    f.write(html_output)