import d2l
from wave_utils.wave_utils import *

pool = d2l.QuestionPool("2_non_ideal_circuit", "non_ideal.csv")

for i in range(50):
    
    a = make_random_signal(20)
    b = make_random_signal(20)
    c = make_random_signal(20)

    # F = ab + c (with delays)
    ab = wavedrom_gate("and", a, b, delay=3)
    f = wavedrom_gate("or", ab, c, delay=2)

    regex_ans = to_regex("f", f)

    q_link = make_wavedrom_link("Topic 13 Question 5", ["a", "b", "c"], [a, b, c], 
                                ["ab", "f"])
    
    a_link = make_wavedrom_link("Topic 13 Question 5 Answer", ["a", "b", "c", "ab", "f"],
                                [a, b, c, ab, f], [])

    q_text = f"<p> The above circuit is NON-ideal, so each gate now has a delay as shown. \
            Click on the link below to open the problem in Watson Wiki. \
            Complete the timing diagram, and then paste all the code \
            into the answer box. </p> <p> {q_link} </p>"

    question = d2l.SAQuestion(q_text)
    # I added labels manually for this one
    question.add_image(f"/imagepools/quantumbeef/non_ideal.png")
    question.add_answer(f"{regex_ans}", is_regex = True)

    question.add_hint('Your wave for F should have 20 characters and look \
                      something like "x...1....0..1..0...."')

    question.add_feedback(f"<p>Here was the right answer: {a_link}</p>")

    pool.add_question(question)

pool.package()