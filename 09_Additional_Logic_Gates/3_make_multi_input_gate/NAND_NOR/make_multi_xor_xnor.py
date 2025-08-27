import d2l
import random
import schemdraw
import schemdraw.logic as sgl
import schemdraw.elements as elm
from schemdraw.parsing import logicparse

pool = d2l.QuestionPool(
        "Make 4 input gate",
        "pool.csv"
        )

# File is the same in other locations, change this variable to select homework # pool (1 = 6,2 = 9_yes,3 = 9_no)

HW6 = 1
HW9Y = 2
HW9N = 3

pool_type = HW9N

if pool_type == 1:
    gates = {
        "AND": "and",
        "OR": "or"
       }   
elif pool_type == 2:
    gates = {
        "XOR" : 'xor',
        "XNOR" : 'xnor'
        }
elif pool_type == 3:
    gates = {
        "NAND" : "nand",
        "NOR" : "nor"
        }

d = schemdraw.Drawing()

for key in gates:
    d = logicparse(f'((A {gates[key]} B) {gates[key]} (C {gates[key]} D))', outlabel='Q')
    d.save(f"{key}_parallel.png")

    d = logicparse(f'((A {gates[key]} (B {gates[key]} (C {gates[key]} D))))', outlabel='Q')
    d.save(f"{key}_cascade.png")


for key2 in gates:
    question_text= f"<p>Logic gates with more than two inputs are \
            typically constructed by combining multiple 2-input \
            gates.</p><p><b> Use the diagram to determine if you can " +\
            f"make a 4-input {key2} using only 2-input {key2} gates.</b></p>"
    question = d2l.MCQuestion( question_text )
    question.add_image(f"/imagepools/alivebeef/{key2}_parallel.png")
    question.add_answer("Yes", 0 if gates[key2] in ('nand', 'nor') else 100)
    question.add_answer("No", 100 if gates[key2] in ('nand', 'nor') else 0)
    pool.add_question(question)

    question = d2l.MCQuestion( question_text )
    question.add_image(f"/imagepools/alivebeef/{key2}_cascade.png")
    question.add_answer("Yes", 0 if gates[key2] in ('nand', 'nor') else 100)
    question.add_answer("No", 100 if gates[key2] in ('nand', 'nor') else 0)
    pool.add_question(question)

pool.dump()
pool.package()
