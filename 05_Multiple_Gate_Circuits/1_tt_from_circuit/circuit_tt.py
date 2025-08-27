import d2l
import random
from schemdraw.parsing import logicparse
from html_tt import html_tt

pool = d2l.QuestionPool(
        "Choose Truth Table from Circuit",
        "pool.csv"
        )

table_info = {
    "0000101110111011" : "0",
    "0000001000100010" : "1",
    "0001000100000001" : "2",
    "0001000100011111" : "3",
    "1110111011101111" : "4",
    "0000100010001000" : "5",
    "1111111111110001" : "6",
    "0111000000000000" : "7"
} 

# Distractors are matched up with answers 
wrong_ans = [
    "0000100111100101",
    "0000010011000101",
    "0000100110000011",
    "0000101001011101",
    "1111011010101110",
    "0001001000010000",
    "1111101111011100",
    "0010101000000000"
]

# These figures can be populated on the server but will be missing labels (ABCD & Q)
d = logicparse('((A or B) and (C or not D))', outlabel='Q')
d.save("ex_0_circ.png")

d = logicparse('((A or B) and (C and not D))', outlabel='Q')
d.save("ex_1_circ.png")

d = logicparse('((not A or B) and (C or D))', outlabel='Q')
d.save("ex_2_circ.png")

d = logicparse('((A and B) or (C and D))', outlabel='Q')
d.save("ex_3_circ.png")

d = logicparse('((A and B) or not (C and D))', outlabel='Q')
d.save("ex_4_circ.png")

d = logicparse('((A or B) and not (C or D))', outlabel='Q')
d.save("ex_5_circ.png")

d = logicparse('((A and B) nor (C and D))', outlabel='Q')
d.save("ex_6_circ.png")

d = logicparse('((A or B) nand (C or D))', outlabel='Q')
d.save("ex_7_circ.png")

for key in table_info.keys():
    question_text= f"<p>The <b>schematic</b> above shows a simple\
            logic circuit with four inputs.</p>" \
            f"<p>Select the truth table below that represents the\
            correct outputs for the circuit:</p>"
    question= d2l.MCQuestion( question_text )
    question.add_image(f"/imagepools/alivebeef/ex_{table_info[key]}_circ.png")

    temp = str(wrong_ans[int(table_info[key])])
    
    correct = html_tt(key,['A','B','C','D','Q'])
    correct_inv = html_tt(''.join('1' if x == '0' else '0' for x in key),['A','B','C','D','Q'])
    distractor = html_tt(temp,['A','B','C','D','Q'])
    distractor_inv = html_tt(''.join('1' if x == '0' else '0' for x in temp),['A','B','C','D','Q'])
    
    question.add_answer(f"{correct}", 100) 
    question.add_answer(f"{correct_inv}", 0)
    question.add_answer(f"{distractor}", 0)
    question.add_answer(f"{distractor_inv}", 0)
    question.add_answer(f"<b>None of the above</b>",0)
    
    pool.add_question(question)

pool.dump()
pool.package()
