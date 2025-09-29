import d2l
import random

pool = d2l.QuestionPool("SR vs. D Latch")

q_text = "Which of the following are true about SR latches and D latches? Select all that apply."

all_answers = [
    ("SR latches are combinational units, while D latches are memory units", False),
    ("SR latches and D latches are both combinational logic units", False),
    ("SR latches and D latches are both memory units", True),
    ("D latches lock the value of the data input when the enable goes high", False),
    ("D latches lock the value of the data input when the enable goes low", True),
    ("Latches can have unknown/undefined output even when there is no delay", True),
    ("A D latch is built by adding an enable input to an SR latch", True),
    ("An SR latch is built by adding an enable input to a D latch", False),
    ("Latches are commonly implemented in real circuitry using NOR and NAND gates", True),
    ("In an SR latch, the output is a function of the current input only", False),
    ("In a D latch, the output is a function of the current input only", False),
    ("SR latches reset their output to 0 when R goes low", False),
    ("SR latches set their output to 1 when S goes high", True)
]

for i in range(10):

    some_answers = random.sample(all_answers, 5)

    question = d2l.MSQuestion(q_text)

    for answer in some_answers:
        question.add_answer(answer[0], answer[1])

    pool.add_question(question)

pool.package()