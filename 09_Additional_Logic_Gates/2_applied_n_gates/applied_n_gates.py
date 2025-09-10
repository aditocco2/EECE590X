import d2l
import random
import schemdraw
import schemdraw.logic as sgl
import schemdraw.elements as elm

pool = d2l.QuestionPool(
        "Choose basic circuit, word prob",
        "pool.csv"
        )

# Change previous simiar question, agree on distinction

question_terms ={
    "1": "during the day if both doors are locked or only one is unlocked.",
    "2": "during the night if both doors are simultaneously unlocked.",
    "3": "day or night when only one of the doors are locked.",
    "4": "during the day if both doors are simultaneously locked.",
    "5": "during the day if both doors are locked or both are unlocked.",
    "6": "during the night if at least 1 door is unlocked."
}        

# Note: I guess time of day is just a distractor

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
d.add(nand_gate)

# NOR
nor_gate = sgl.Nor().at((0,-2))
d.add(nor_gate)

# XNOR 
xnor_gate = sgl.Xnor().at((2.5,-2))
d.add(xnor_gate)

# AND
and_gate = sgl.And().at((2.5,0))
d.add(and_gate) 

# XOR
xor_gate = sgl.Xor().at((5,0))
d.add(xor_gate) 

# OR
or_gate = sgl.Or().at((5,-2))
d.add(or_gate)

d.draw()
#d.save("n_base_circuits_no_labels.png") # is already generated for an earlier hw

for key in question_terms.keys():
    question_text= f"<p>The local candy store owner wants to secure the \
            front and back door of their shop. They wire the \
            system so that when the alarm is set and a door is unlocked \
            its sensor outputs high ('1'), and low ('0') otherwise.</p>" +\
            f"<p>They want the silent alarm to sound {question_terms[key]}</p>" +\
            f"<p><b>If they ask you to build the circuit, which gate \
            should you use?</b></p>"
    question = d2l.MCQuestion( question_text )
    question.add_image("/imagepools/alivebeef/n_base_circuits_1.png")
    for key2 in question_terms.keys():
        # Bruh, you made it 1 instead of 100
        question.add_answer(f"{key2}", 100 if key2 in key else 0) #is_correct = key )
    pool.add_question(question)

pool.dump()
pool.package()
