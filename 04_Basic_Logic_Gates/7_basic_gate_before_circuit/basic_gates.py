import d2l
import random
import schemdraw
import schemdraw.logic as sgl
import schemdraw.elements as elm

pool = d2l.QuestionPool(
        "Choose basic gate",
        "pool.csv"
        )

question_terms ={
    "A": "Her security circuit is designed to receive a logic '1' when\
            both the window is open and motion is detected",
    "B": "Her security circuit is designed to receive a logic '1' when\
            the window is open or motion is detected, or both",
    "C": "Her security circuit is designed to receive a logic '1' when\
            the window is closed",
    "D": "Her security circuit is designed to receive a logic '1' when\
            only the window is open or only motion is detected"
}        

d = schemdraw.Drawing()
# Answer Labels - add back in when schemdraw is updated on server

#d.add(schemdraw.elements.Label('A', color='red').at((1.25, -1))) 
#d.add(schemdraw.elements.Label('B', color='red').at((4.75, -1))) 
#d.add(schemdraw.elements.Label('C', color='red').at((1.25, -3))) 
#d.add(schemdraw.elements.Label('D', color='red').at((4.75, -3))) 

# AND - A
and_gate = sgl.And().at((0.5,0))
d.add(and_gate) 

# NOT - C
not_gate_1 = sgl.Not().at((0, -2))
d.add(not_gate_1) 

# OR - B
or_gate = sgl.Or().at((4,0))
d.add(or_gate) 

# XOR - D
xor_gate = sgl.Xor().at((4,-2))
d.add(xor_gate) 

d.draw()
d.save("base_gates_no_labels.png")

for key in question_terms.keys():
    if key == "D": # Do not ask xor as question, they have not been taught
        break
    else:
        if key not in "C":
            second_input = "She also adds a motion detector that outputs a\
                '1' when motion is detected in the room, and '0' otherwise."
        else:
            second_input = ""
    
        question_text = f"<p>An engineer decides to design a simple\
        security system for her home before she goes on vacation.\
        She puts a sensor on her first floor window that outputs a\
        logic '1' when the window is opened, and a '0' otherwise.</p>" \
        f"{second_input}"\
        f"<p>{question_terms[key]}.</p>"\
        f"<p><b>What type of gate should be used to\
        interface the sensor(s) with the security system?</b></p>"\
        f"<p>Select One:</p>"
        question = d2l.MCQuestion( question_text )
        question.add_image("/imagepools/alivebeef/base_gates.png")
        for key2 in question_terms.keys():
            question.add_answer(f"{key2}", 100 if key2 in key else 0)
        pool.add_question(question)

pool.dump()
pool.package()
