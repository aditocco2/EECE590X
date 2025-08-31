# Makes a pool of 10 random questions for the same NON-ideal circuit

import d2l
from wave_utils import *

pool = d2l.QuestionPool("2_non_ideal_circuit", "non_ideal.csv")

for i in range(10):
    
    a = make_random_signal(20)
    b = make_random_signal(20)

    # F = ab + a'b'
    a_and_b = wavedrom_gate("and", a, b, delay=3)
    not_a = wavedrom_gate("not", a, delay=1)
    not_b = wavedrom_gate("not", b, delay=1)
    not_a_and_not_b = wavedrom_gate("and", not_a, not_b, delay=3)
    f = wavedrom_gate("or", a_and_b, not_a_and_not_b, delay=2)

    regex_ans = to_regex("f", f)

    q_link = make_question_link(f"Topic 13 Question 2", ["a", "b"], [a, b], 
                                ["a'", "b'", "ab", "a'b'", "F"])

    q_text = f"<p> The above circuit is NON-ideal, so each gate now has a delay as shown. \
            Click on the link below to open the problem in Watson Wiki. \
            Complete the timing diagram, and then paste all the code \
            into the answer box. </p> <p> {q_link} </p>"

    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/non_ideal.png")
    question.add_answer(f"{regex_ans}", is_regex = True)

    pool.add_question(question)

pool.package()