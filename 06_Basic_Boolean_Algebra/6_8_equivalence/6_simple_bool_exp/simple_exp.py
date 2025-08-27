import d2l
import random
from schemdraw.parsing import logicparse

pool = d2l.QuestionPool(
        "Choose expression equivalent to circuit",
        "pool.csv"
        )

q_circuit = {
    "exp_1.png" : "ab+ac",
    "exp_2.png" : "(a+b)(a+c)",
    "exp_3.png" : "a+b+c",
    "exp_4.png" : "abc"
    } 

# These figures can be populated on the server (doesn't use newest code)
d = logicparse('((A and B) or (A and C))', outlabel='Q')
d.save("exp_1.png")

d = logicparse('((A or B) and (A or C))', outlabel='Q')
d.save("exp_2.png")

d = logicparse('(A or B or C)', outlabel='Q')
d.save("exp_3.png")

d = logicparse('(A and B and C)', outlabel='Q')
d.save("exp_4.png")

for key in q_circuit.keys():
    question_text= f"<p>The <i>schematic</i> above describes a binary\
            digital system whose output Q is a function of its four \
            inputs:</p>" \
            f"<p>Construct a <b>Boolean expression</b> which is equivalent\
            to output Q.</p>"
    question= d2l.MCQuestion( question_text )
    question.add_image(f"/imagepools/alivebeef/{key}")

    for key2 in q_circuit.keys():      
        question.add_answer(f"{q_circuit[key2]}", 1 if key2 == key else 0) 
       
    pool.add_question(question)

pool.dump()
pool.package()
