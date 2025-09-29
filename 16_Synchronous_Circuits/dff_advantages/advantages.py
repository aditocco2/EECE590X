import d2l
import random

pool = d2l.QuestionPool("Advantages of Flip-Flops")

q_text = "Which of the following are advantages of flip flops over latches? \
            Select all that apply."

all_answers = [
    ("FFs are more glitch-resistant", True),
    ("FFs can be used to synchronize inputs and outputs", True),
    ("FFs only sample on the rising edge of the control signal", True),
    ("FFs are less likely to produce undefined/unknown output", True),
    ("FFs can be used to remember what an input was a while ago", True),
    ("FFs can be set and reset", False),
    ("FFs can reflect changes in input instantly when they are enabled", False),
    ("FFs are more compact and require less gates", False)
    # Maybe add some more?
]

for i in range(10):

    some_answers = random.sample(all_answers, 5)

    question = d2l.MSQuestion(q_text)

    for answer in some_answers:
        question.add_answer(answer[0], answer[1])

    pool.add_question(question)

pool.package()