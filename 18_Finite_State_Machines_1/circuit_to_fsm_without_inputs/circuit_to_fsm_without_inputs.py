# After running this script, the following things must be done:
#       Draw the circuit diagrams using the expressions in outputs.txt
#       Add the images manually to the questions and answers in Brightspace

import d2l
from fsm.fsm_class import FSM

# Clear outputs.txt file before adding new data
with open("outputs.txt", "w") as file:
    pass

pool = d2l.QuestionPool("Circuit to FSM (no inputs)")

hint = ("As an intermediate step, make a truth table for the next state " +
        "and the outputs, based on the current state.")

variants = "ABCD"

for q_letter in variants:

    fsm_name = f"FSM_18_{q_letter}"
    fsm_filename = f"{fsm_name}.txt"

    fsm = FSM(fsm_filename, fsm_name)

    # Write output expressions so I can reference them while drawing diagrams
    fsm.write_output_expressions_to_file("outputs.txt")

    # Placeholder for circuit image of the current variant
    q_text = (f"(put circuit image {q_letter} here)\n" +
        "What is the correct finite state machine model for the circuit above?")

    question = d2l.MCQuestion(q_text, shuffle=False)
    question.add_hint(hint)

    # Put placeholders for the images for all variants (A, B, C, and D) as the answer
    for a_letter in variants:

        points = 100 if q_letter == a_letter else 0

        question.add_answer(f"(Put FSM image {a_letter} here)", points)

    pool.add_question(question)

pool.package()