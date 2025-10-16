import d2l
import os
from fsm.fsm_class import FSM

pool = d2l.QuestionPool("Find Intended FSM Pattern")

# pick up sequences from the image names in the folder
image_names = [f for f in os.listdir(".") if f.endswith(".png")]
text_names = [s.replace(".png", ".txt") for s in image_names]
sequences = [s.replace("FSM_19_", "").replace(".png", "")
             for s in image_names]

for image, text, sequence in zip(image_names, text_names, sequences):
    
    # Make sure the FSM is properly specified
    fsm = FSM(text)
    if not fsm.is_properly_specified():
        raise Exception(f"{text} is not properly specified")
    
    # Make sure the pattern works starting from every state in the FSM
    for state in fsm.state_names:
        end_state = fsm.follow(sequence, state)
        end_out = fsm.find_output(end_state, "F")
        if end_out != "1":
            raise Exception(f"{text} doesn't follow the pattern {sequence} for state {state}")
    
    # Now make the questions
    q_text = "Which pattern on the input A will make the FSM above output 1?"
    image_link = f"/imagepools/quantumbeef/{image}"
    # Start of string, anything non-numeric, answer,
    # anything else non-numeric, end of string
    regex_ans = rf"^[^0-9]*{sequence}[^0-9]*$"
    
    question = d2l.SAQuestion(q_text)
    question.add_image(image_link)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(sequence)

    pool.add_question(question)

pool.package()
