import d2l
import random

pool = d2l.QuestionPool("SR vs. D Latch")

q_text = "Which of the following are true about SR latches and D latches? Select all that apply."

all_answers = [
    ("SR latches and D latches are both combinational logic units", False),
    ("SR latches are combinational units, while D latches are memory units", False),
    ("SR latches are memory units, while D latches are combinational units", False),
    ("SR latches and D latches are both memory units", True),

    ("SR latches and D latches both only use control inputs", False),
    ("SR latches only use control inputs, while D latches use a control and a data input", True),
    ("SR latches use a control and a data input, while D latches only use control inputs", False),
    ("SR latches and D latches both use a control and data input", False),
    
    ("D latches hold the value of the data input when the enable goes high", False),
    ("D latches hold the value of the data input when the enable goes low", True),

    ("A D latch is built by adding an enable input to an SR latch", True),
    ("An SR latch is built by adding an enable input to a D latch", False),

    ("Both SR and D latches are commonly implemented in real circuitry using NOR and NAND gates", True),
]

for i in range(10):

    some_answers = random.sample(all_answers, 5)

    question = d2l.MSQuestion(q_text)

    for answer in some_answers:
        question.add_answer(answer[0], answer[1])

    pool.add_question(question)

pool.package()