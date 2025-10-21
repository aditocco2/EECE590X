import d2l
import random
from fsm.fsm import FSM

variants = "ABCDEF"

pool = d2l.QuestionPool("Find Output Expressions With Reset")

for letter in variants:

    text_file = f"FSM_22_{letter}.txt"
    image_link = f"/imagepools/quantumbeef/FSM_22_{letter}.png"

    hint = "Q2 and Q0 are the most significant and least significant bits of the state respectively."

    fsm = FSM(text_file)
    out_exp = fsm.find_output_expressions(include_reset=False)
    reset_exp = fsm.find_output_expressions(include_reset=True)
    reset_state = fsm.reset_state

    # Assemble the question text:
    q_text = "<p> The trivial FSM above always outputs the pattern 000101. \
        Suppose that you have already found the logic for the next state \
        and output to be the following: </p><p>"
    for out in out_exp:
        q_text += f"{out} = {out_exp[out]} <br>" # Q2 = Q1Q0 and so on
    q_text += f"</p><p> You now want to add a reset input <i>r</i> that forces the FSM \
        into state <b>{reset_state}</b>. What would the new logic expressions be? Match them below.</p>"
    
    # Make all the answers with distractors
    answers = []
    for out in reset_exp:
        exp = reset_exp[out]
        answers.append(exp)
        # Modify the string for distractors
        if exp.endswith(" + r"):
            exp = exp.replace(" + r", "r'")
        elif exp.endswith(")r'"):
            exp = exp.replace("r'", " + r")
        answers.append(exp)

    random.shuffle(answers)

    # Now make the question and add its answers
    question = d2l.MQuestion(q_text)
    question.add_image(image_link)
    question.add_hint(hint)
    # Add all possible choices first
    for answer in answers:
        question.add_answer(choice = answer)
    # Then add the correct ones with their matches
    for out in reset_exp:
        question.add_answer(out, reset_exp[out])
    
    pool.add_question(question)

pool.package()


