import d2l
import random
from fsm.fsm import FSM

pool = d2l.QuestionPool("Follow FSM Pattern")

fsm = FSM("FSM_19_E.txt")
image = "FSM_19_E.png"
image_link = f"/imagepools/quantumbeef/{image}"

sequence_length = 8

# for row in fsm.rows:
#     print(row)

if not fsm.is_properly_specified():
    raise Exception("FSM is not properly specified")

for state in fsm.state_names:

    # Make 5 random binary numbers
    sequences = []
    for _ in range(5):
        sequence = random.randint(0, 2 ** sequence_length - 1)
        sequence = f"{sequence:0{sequence_length}b}"
        sequences.append(sequence)

    # Make a variant for each of these numbers
    for sequence in sequences:
        
        end_state, _, _ = fsm.follow(sequence, state)

        q_text = f"<p>If the FSM above starts in state {state} and has an input \
            sequence of {sequence}, what state will it end in?</p>"
        regex_ans = rf"^[^0-9]*{end_state}[^0-9]*$"

        question = d2l.SAQuestion(q_text)
        question.add_image(image_link)
        question.add_answer(regex_ans, is_regex=True)
        question.add_feedback(end_state)

        pool.add_question(question)

pool.package()
        