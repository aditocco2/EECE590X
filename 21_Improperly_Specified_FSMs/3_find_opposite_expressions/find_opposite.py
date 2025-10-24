# IMPORTANT:
# When building these FSMs in FSM Explorer, you gotta specify the placeholders themselves as inputs too. 
# (double click on the canvas with the select tool and type your list like "a, b, c, F, G, H, I")

import d2l
from fsm.fsm import FSM
from logic_utils.logic_utils import opposite

pool = d2l.QuestionPool("Find Opposite Expressions")

fsm_letters = "FG"
placeholders = "FGHI"

for fsm_letter in fsm_letters:

    text_file = f"FSM_21_{fsm_letter}.txt"
    image_link = f"/imagepools/quantumbeef/FSM_21_{fsm_letter}.png"

    fsm = FSM(text_file)
    
    # Keep track of every answer for distractors
    all_answers = {}

    # For every state:
    for d in fsm.state_data:

        # Get the placeholder (like "F") and the expression we're looking for
        for arc in d["arcs"]:
            if arc["expression"][1] in placeholders:
                placeholder = arc["expression"][1]
            else:
                right_answer = opposite(fsm.input_names, arc["expression"])
        
        all_answers[placeholder] = right_answer

    # Now make the questions
    for placeholder in placeholders:
    
        q_text = f"<p> In order to make the FSM above properly specified, what expression would \
               need to go on the arc labeled <b>{placeholder}</b>?"
        question = d2l.MCQuestion(q_text)
        question.add_image(image_link)
        
        for answer in all_answers.values():

            points = 100 if all_answers[placeholder] == answer else 0
            question.add_answer(answer, points)

        pool.add_question(question)

pool.package()


        

        
