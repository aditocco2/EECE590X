import d2l
from html_utils.html_utils import *

pool = d2l.QuestionPool("Magnitude Comparator Using Subtraction")

with open("yapping_3.html", "r") as f:
    q_text_base = f.read()

answers = [
    "<p>If the most significant bit of R is 1</p>",
    "<p>If the most significant bit of R is 0</p>",
    f"<p>If the most significant bit of R is 0 {italic("and the rest of R is not all 0")}</p>",
    f"<p>If the most significant bit of R is 1 {italic("or if R is all 0")}</p>"
]

# A < B when the MSB of R is 1 (A-B is negative)
q_text = q_text_base.replace("[REPLACE]", "A is less than B")
question = d2l.MCQuestion(q_text)
for i in range(4):
    question.add_answer(answers[i], 100 if i==0 else 0)
pool.add_question(question)

# A >= B when the MSB of R is 0 (A-B is positive or 0)
q_text = q_text_base.replace("[REPLACE]", "A is greater than or equal to B")
question = d2l.MCQuestion(q_text)
for i in range(4):
    question.add_answer(answers[i], 100 if i==1 else 0)
pool.add_question(question)

# A > B when the MSB of R is 0 and the rest of R is not all 0 (A-B is positive but not 0)
q_text = q_text_base.replace("[REPLACE]", "A is greater than B")
question = d2l.MCQuestion(q_text)
for i in range(4):
    question.add_answer(answers[i], 100 if i==2 else 0)
pool.add_question(question)

# A <= B when the MSB of R is 1 or if R=0 (A-B is negative or 0)
q_text = q_text_base.replace("[REPLACE]", "A is less than or equal to B")
question = d2l.MCQuestion(q_text)
for i in range(4):
    question.add_answer(answers[i], 100 if i==3 else 0)
pool.add_question(question)

pool.package()