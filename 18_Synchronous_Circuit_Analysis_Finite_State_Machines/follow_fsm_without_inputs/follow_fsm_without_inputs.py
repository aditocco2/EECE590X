import d2l
from fsm.fsm import FSM

pool = d2l.QuestionPool("Follow FSM from circuit")


for letter in "ABCD":

    fsm_filename = f"FSM_18_{letter}.txt"
    image_name = f"circ_18_{letter}.png" # made manually for previous question

    fsm = FSM(fsm_filename)

    # 16 variants total
    for steps in range(4, 8):

        ending_state, _, _ = fsm.follow(steps, "00")
 
        q_text = f"<p>Suppose the FSM represented by the circuit above is originally \
            in state 00 (Q1 = 0 and Q0 = 0). At what state will the FSM be in \
                <i>{steps}</i> clock cycles?</p>"
        image_link = f"/imagepools/quantumbeef/{image_name}"
        
        # Start of string, anything non-numeric, answer,
        # anything else non-numeric, end of string
        regex_ans = rf"^[^0-9]*{ending_state}[^0-9]*$"
        feedback = f"It will be in state {ending_state}"

        question = d2l.SAQuestion(q_text)
        question.add_image(image_link)
        question.add_answer(regex_ans, is_regex=True)
        question.add_feedback(feedback)

        pool.add_question(question)

pool.package()