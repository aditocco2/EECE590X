import d2l
from wave_utils.wave_utils import *

pool = d2l.QuestionPool("ideal_circuit", "ideal.csv")

# Make 50 variants
for i in range(50):
    
    a = make_random_signal(20)
    b = make_random_signal(20)
    c = make_random_signal(20)

    # F = ab + c
    ab = wavedrom_gate("and", a, b, delay=0)
    f = wavedrom_gate("or", ab, c, delay=0)

    regex_ans = to_regex("f", f)

    # Make Watson Wiki links with GitHub alternates
    q_link = make_wavedrom_link("Topic 13 Question 4", ["a", "b", "c"], [a, b, c], 
                                ["ab", "f"], link_text="WaveDrom Link")
    a_link = make_wavedrom_link("Topic 13 Question 4 Answer", ["a", "b", "c", "ab", "f"],
                                [a, b, c, ab, f], [])

    q_text = f"<p> The above circuit is ideal and ignores gate delays. \
            Click on the link below to open the problem in WaveDrom. \
            Complete the timing diagram, and then paste <b>all</b> the code \
            into the answer box. </p> <p> {q_link} </p>"
    
    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/ideal.png")
    question.add_answer(f"{regex_ans}", is_regex = True)

    question.add_hint('Your wave for F should have 20 characters and look \
                      something like "00000111110001110000" (or "0....1....0..1..0...")')

    question.add_feedback(f"<p>Here was the right answer: {a_link}</p>")

    pool.add_question(question)

pool.package()