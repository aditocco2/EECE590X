# Makes a question pool for an ideal circuit consisting of one XOR gate

import d2l
from wave_utils import *

a = make_random_signal(20)
b = make_random_signal(20)

f = wavedrom_gate("xor", a, b, 0)

regex_ans = to_regex("f", f)

# Just to look at it
print(f"a: {a}\nb: {b}\nf: {f}")

q_link = make_question_link("Question 1", ["a", "b"], [a, b], ["F"])

pool = d2l.QuestionPool("WaveDrom Ideal XOR", "xor.csv")
q_text = f"<p> The above circuit is ideal and ignores gate delays. \
        Click on the link below to open the problem in Watson Wiki. \
        Complete the timing diagram, and then paste your whole code \
        into the answer box. </p> <p> {q_link} </p>"

question = d2l.SAQuestion(q_text)
question.add_image(f"/imagepools/quantumbeef/xor.png")
question.add_answer(f"{regex_ans}", is_regex = True)

pool.add_question(question)

pool.package()