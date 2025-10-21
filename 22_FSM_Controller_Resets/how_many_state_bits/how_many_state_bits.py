import d2l
import math

pool = d2l.QuestionPool("How Many State Bits")

for num_states in range(2, 17): # 2 to 16

    q_text = f"Suppose you are using the controller model above to implement \
        an FSM with {num_states} states. How many bits would the state register need?"

    num_state_bits = math.ceil(math.log2(num_states))
    regex_ans = rf"^[^0-9]*{num_state_bits}[^0-9]*$"

    question = d2l.SAQuestion(q_text)
    question.add_image("/imagepools/quantumbeef/generic_controller_model.png")
    question.add_answer(regex_ans, is_regex=True)

    question.add_feedback(f"There will be {num_state_bits} state bits")

    pool.add_question(question)

pool.package()