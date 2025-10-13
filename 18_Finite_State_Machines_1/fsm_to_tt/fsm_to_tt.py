import d2l
from fsm.fsm_class import FSM

pool = d2l.QuestionPool("FSM to Truth Table")

variants = "EFGH"

# Make all 4 TTs at once so they can all be in the question's answers
tts = {}
for q_letter in variants:
    fsm_name = f"FSM_18_{q_letter}"
    fsm_filename = fsm_name + ".txt"
    fsm = FSM(fsm_filename, fsm_name)
    tts[q_letter] = fsm.make_html_truth_table()

    # To make sure it's properly specified
    # print(fsm_name)
    # for row in fsm.rows:
    #     print(row)  

# Now make the questions   
for q_letter in variants:

    q_text = "What is the correct truth table for the FSM model above?"
    hint = "Q and Q+ are the state and next state respectively."
    image_link = f"/imagepools/quantumbeef/FSM_18_{q_letter}.png"

    question = d2l.MCQuestion(q_text)
    question.add_hint(hint)
    question.add_image(image_link)

    # Put the TTs from all variants (E, F, G, and H) as the answers
    for a_letter in tts:

        tt = tts[a_letter]
        points = 100 if q_letter == a_letter else 0

        question.add_answer(tt, points)

    pool.add_question(question)

pool.package()




