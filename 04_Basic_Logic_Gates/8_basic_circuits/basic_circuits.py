import d2l
import random
import schemdraw
import schemdraw.logic as sgl
import schemdraw.elements as elm

pool = d2l.QuestionPool(
        "Choose basic circuit",
        "pool.csv"
        )

question_terms ={
    "A": "send a '0' value alarm only when both <u>the window is open</u> and <u>there is motion detected</u>",
    "B": "send a '1' value alarm only when both <u>the window is open</u> and <u>there is motion detected</u>",
    "C": "send a '1' value alarm only when <u>the window is open</u> or <u>there is motion detected</u>",
    "D": "send a '1' value alarm only when both <u>the window is closed</u> and <u>no motion is detected</u>",
    "E": "send a '1' value alarm when either both <u>the window is open</u> and <u>there is motion detected</u> or <u>the window is closed</u> and <u>no motion is detected</u>",
    "F": "send a '1' value alarm when there is at least <u>a window is open</u> or <u>there is motion detected</u>"
}        

d = schemdraw.Drawing()
# Answer Labels - does not work on server version of schemdraw

d.add(schemdraw.elements.Label('B', color='red').at((2.5, -1)))
d.add(schemdraw.elements.Label('A', color='red').at((8.5, -1)))
d.add(schemdraw.elements.Label('C', color='red').at((14.5, -1)))
d.add(schemdraw.elements.Label('D', color='red').at((2.5, -3)))
d.add(schemdraw.elements.Label('E', color='red').at((8.5, -3)))
d.add(schemdraw.elements.Label('F', color='red').at((14.5, -3)))

# NAND
and_gate = sgl.And()
d.add(and_gate)
not_gate_1 = sgl.Not().right()
d.add(not_gate_1)
d.add(sgl.Line().at(and_gate.out).to(not_gate_1.in1))

# NOR
or_gate = sgl.Or().at((0,-2))
d.add(or_gate) 
not_gate_2 = sgl.Not().right()
d.add(not_gate_2)
d.add(sgl.Line().at(or_gate.out).to(not_gate_2.in1))

# XNOR
xor_gate = sgl.Xor().at((6,-2))
d.add(xor_gate) 
not_gate_3 = sgl.Not().right()
d.add(not_gate_3) 
d.add(sgl.Line().at(xor_gate.out).to(not_gate_3.in1))

# AND
and_gate_2 = sgl.And().at((6,0))
d.add(and_gate_2) 
d.add(sgl.Line().at(and_gate_2.out).to((11, 0)))

# XOR
xor_gate_2 = sgl.Xor().at((12,0))
d.add(xor_gate_2) 
d.add(sgl.Line().at(xor_gate_2.out).to((17, 0)))

# OR
or_gate_2 = sgl.Or().at((12,-2))
d.add(or_gate_2) 
d.add(sgl.Line().at(or_gate_2.out).to((17, -2)))

d.draw()
d.save("base_circuits_no_labels.png")

for key in question_terms.keys():
    if key in ("C" , "E"): # remove xor and xnor
        continue
    else:
        question_text= f"<p>The <i>safety circuit</i> from the previous question has two inputs:</p>" \
                f"<p><b>X:</b>    A <b><u>window open signal</u></b>, which is '1' if\
                the window is open, and '0' if it is closed.</p>"\
                f"<p><b>Y:</b>    A <b><u>motion detection signal</u></b>, which is '1' when motion is detected inside the room,\
                and '0' otherwise.</p>"\
                f"<p>Choose which circuit above would {question_terms[key]}.</p>"
        question = d2l.MCQuestion( question_text )
        question.add_image("/imagepools/alivebeef/base_circuits.png")
        for key2 in question_terms.keys():
            question.add_answer(f"{key2}", 100 if key2 in key else 0) #is_correct = key )
        pool.add_question(question)

pool.dump()
pool.package()
