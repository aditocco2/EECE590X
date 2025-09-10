# Makes a pool of 10 random questions for the same ideal circuit

import d2l
from wave_utils.wave_utils import *

pool = d2l.QuestionPool("1_ideal_circuit", "ideal.csv")

for i in range(50):
    
    a = make_random_signal(20)
    b = make_random_signal(20)

    # F = ab + a'b'
    a_and_b = wavedrom_gate("and", a, b)
    not_a = wavedrom_gate("not", a)
    not_b = wavedrom_gate("not", b)
    not_a_and_not_b = wavedrom_gate("and", not_a, not_b)
    f = wavedrom_gate("or", a_and_b, not_a_and_not_b)

    regex_ans = to_regex("f", f)

    q_link = make_question_link("Topic 13 Question 1", ["a", "b"], [a, b], 
                                ["a'", "b'", "ab", "a'b'", "F"])

    q_text = f"<p> The above circuit is ideal and ignores gate delays. \
            Click on the link below to open the problem in Watson Wiki. \
            Complete the timing diagram, and then paste all the code \
            into the answer box. </p> <p> {q_link} </p>"

    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/ideal.png")
    question.add_answer(f"{regex_ans}", is_regex = True)

    # To Do: add feedback (right answer as link)
    # question.add_feedback()

    pool.add_question(question)

pool.package()