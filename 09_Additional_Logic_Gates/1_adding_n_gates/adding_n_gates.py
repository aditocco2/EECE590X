import d2l
import random
import schemdraw
import schemdraw.logic as sgl
import schemdraw.elements as elm

pool = d2l.QuestionPool(
        "Choose basic circuit",
        "pool.csv"
        )

# Change previous simiar question, agree on distinction

question_terms ={
    "NAND": "When neither of its inputs are 1 or only one of its inputs are 1",
    "AND": "Only when both inputs are 1",
    "XOR": "When only one of its inputs are 1",
    "NOR": "Only when neither of its inputs are 1",
    "XNOR": "When neither or both of its inputs are 1",
    "OR" : "When at least one of its inputs are 1"
}        

d = schemdraw.Drawing()
# Answer Labels - update schemdraw version to use
#d.add(schemdraw.elements.Label('1', color='red').at((0.75, -1))) 
#d.add(schemdraw.elements.Label('2', color='red').at((3.25, -1))) 
#d.add(schemdraw.elements.Label('3', color='red').at((5.75, -1))) 
#d.add(schemdraw.elements.Label('4', color='red').at((0.75, -3))) 
#d.add(schemdraw.elements.Label('5', color='red').at((3.25, -3))) 
#d.add(schemdraw.elements.Label('6', color='red').at((5.75, -3))) 

# NAND
nand_gate = sgl.Nand()
d.add(nand_gate)  # Add AND gate to the drawing

# NOR
nor_gate = sgl.Nor().at((0,-2))
d.add(nor_gate)  # Add OR gate to the drawing

# XNOR 
xnor_gate = sgl.Xnor().at((2.5,-2))
d.add(xnor_gate)  # Add OR gate to the drawing

# AND
and_gate = sgl.And().at((2.5,0))
d.add(and_gate)  # Add OR gate to the drawing

# XOR
xor_gate = sgl.Xor().at((5,0))
d.add(xor_gate)  # Add OR gate to the drawing

# OR
or_gate = sgl.Or().at((5,-2))
d.add(or_gate)  # Add OR gate to the drawing

d.draw()
d.save("n_base_circuits_no_labels.png")

question_text= f"<p>Select which gate should be used to produce a HIGH \
        signal for each scenario below:</p>"
question = d2l.MQuestion( question_text )
question.add_image("/imagepools/alivebeef/n_base_circuits_1.png")
for key2 in question_terms.keys():
    question.add_answer(question_terms[key2],key2)
pool.add_question(question)

pool.dump()
pool.package()
