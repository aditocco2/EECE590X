import d2l

pool = d2l.QuestionPool("Find State Register SR Signals")

image_link = "/imagepools/quantumbeef/state_register_3b_unknown.png"

# All 3-bit binary numbers from 000 to 111
reset_states = [f"{i:0{3}b}" for i in range(0, 8)]

for state in reset_states:

    q_text = f"<p> Suppose you are using flip-flops with synchronous set and reset inputs \
        to implement a 3-bit state register as shown above. \
            You want the FSM to reset to state <b>{state}</b> when a signal <i>r</i> is high. \
                What signals should go into the flip-flops' set and reset inputs? \
                Match them below. </p>"
    
    question = d2l.MQuestion(q_text)
    question.add_image(image_link)
    
    # Initialize all answers, as some will never be used
    for answer in ["r", "r'", "Constant 1", "Constant 0"]:
        question.add_answer(choice=answer)
    
    # Now analyze the state to get the right answers
    if state[0] == "1": #Q2
        question.add_answer("A", "r")
        question.add_answer("B", "Constant 0")
    else:
        question.add_answer("A", "Constant 0")
        question.add_answer("B", "r")
    
    if state[1] == "1": #Q1
        question.add_answer("C", "r")
        question.add_answer("D", "Constant 0")
    else:
        question.add_answer("C", "Constant 0")
        question.add_answer("D", "r")

    if state[2] == "1": #Q0
        question.add_answer("E", "r")
        question.add_answer("F", "Constant 0")
    else:
        question.add_answer("E", "Constant 0")
        question.add_answer("F", "r")

    pool.add_question(question)

pool.package()