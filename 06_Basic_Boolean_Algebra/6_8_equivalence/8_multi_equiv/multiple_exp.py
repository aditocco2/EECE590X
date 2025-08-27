import d2l
import random
from schemdraw.parsing import logicparse

pool = d2l.QuestionPool(
        "Choose expressions with equivalent function"
        "pool.csv"
        )

# First 2 are the correct and the last two are distractors
q_circuit = { ## check that example           vvvvvvvvvvvv
    "mult_exp_1.png" : ("ab+(c+d)", "d+ab+c","(c+a)(c+b)+d", "(a+d)(b+c)", "a+b+c+d"),
    "mult_exp_2.png" : ("(a+b)(cd)", "acd+bcd", "abcd", "(ab)c+(ab)d"),
    "mult_exp_3.png" : ("a+b+c+d", "(a+d)+c+b", "(abcd)", "(((ab)c)d)"), 
    "mult_exp_4.png" : ("abcd", "a(bc)d", "(cd)+b+a", "a+b+cd")
    } 

# These figures can be populated on the server but will be missing io labels
d = logicparse('((A and B) or (C or D))', outlabel='Q')
d.save("mult_exp_1.png")

d = logicparse('((A or B) and (C and D))', outlabel='Q')
d.save("mult_exp_2.png")

d = logicparse('(((A or B) or C) or D)', outlabel='Q')
d.save("mult_exp_3.png")

d = logicparse('(A and (B and (C and D)))', outlabel='Q')
d.save("mult_exp_4.png")

for key in q_circuit.keys():
    question_text= f"<p>Select <b>ALL</b> of the expressions that are \
            functionally equivalent to the circuit in the schematic \
            above.</p>" 
    question= d2l.MSQuestion( question_text )
    question.add_image(f"/imagepools/alivebeef/{key}")
    question.add_answer(f"{q_circuit[key][0]}", 1) 
    question.add_answer(f"{q_circuit[key][1]}", 1) 
    question.add_answer(f"{q_circuit[key][2]}", 0)
    question.add_answer(f"{q_circuit[key][3]}", 0)
    pool.add_question(question)

pool.dump()
pool.package()
