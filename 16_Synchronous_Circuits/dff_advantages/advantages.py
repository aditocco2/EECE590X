import d2l
import random

pool = d2l.QuestionPool("Advantages of Flip-Flops")

q_text = "Which of the following are advantages of flip flops over latches? \
            Select all that apply."

all_answers = [
    ("FFs do not pass glitches from input to output", True),
    ("FFs can be used to synchronize input and output changes with a control signal", True),
    ("FFs only pass data from input and output on the edge of the control signal", True),
    ("FFs can be chained together to introduce a fixed delay", True),
    ("FFs are less likely to produce undefined/unknown output", True),
    ("FFs can continuously pass data from input to output whenever they are enabled", False),
    ("FFs are more compact and require less gates", False),
    ("FFs can be set and reset with different control signals", False)
]

for i in range(10):

    some_answers = random.sample(all_answers, 5)

    question = d2l.MSQuestion(q_text)

    for answer in some_answers:
        question.add_answer(answer[0], answer[1])

    pool.add_question(question)

pool.package()