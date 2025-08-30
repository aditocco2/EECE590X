import d2l
import random

pool = d2l.QuestionPool(
        "Choose basic circuit (fixed)",
        "pool2.csv"
        )

question_terms ={
    "A": "<b>'1'</b> when both the window is open and there is motion detected",
    "B": "<b>'1'</b> when either the window is open or there is motion detected (or both)",
    "C": "<b>'0'</b> when both the window is open and there is motion detected",
    "D": "<b>'1'</b> only when the window is closed and no motion is detected",
}        

for key in question_terms.keys():
    
    question_text = f"<p>A security system has two inputs. The first input is X, a 'window open' signal \
                    which is 1 if a window is open and 0 if it's closed. The second input is \
                    Y, a 'motion detected' signal that is 1 if motion is detected and 0 otherwise.</p> \
                    <p>Choose a system above whose output F will be {question_terms[key]}.</p>"


    question = d2l.MCQuestion( question_text , shuffle=False)
    question.add_image("/imagepools/quantumbeef/basic_circuits_4_systems.png")
    for key2 in question_terms.keys():
        question.add_answer(f"{key2}", 100 if key2 in key else 0,) 
    pool.add_question(question)

# pool.dump()
pool.package()
