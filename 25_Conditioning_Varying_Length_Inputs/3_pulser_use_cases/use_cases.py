import d2l
import random

q_text = f"In which of the following scenarios would a pulser be helpful? Select all that apply."

# Unfinished

correct = [
    ("Counting how many times a button has been pressed", True),
    ("Adding 1 to a register every time an external signal toggles", True)
]

wrong = [
    ("Counting how many nanoseconds a signal goes high", False),
    ("Determining whether two registers have the same value", False),
    ("Determining whether one register has a greater value than the other", False),
    ("Adding 1 to a register for every clock cycle", False)
]

pool = d2l.QuestionPool("Pulser Use Cases")

for _ in range(8):

    # Sample randomly with at least one correct answer
    all = correct + wrong
    choices = [all.pop(random.randrange(len(correct)))] + random.sample(all, 3)

    question = d2l.MSQuestion(q_text)

    for choice in choices:
        answer = choice[0]
        points = 100 if choice[1] else 0
        question.add_answer(answer, points)
    
    pool.add_question(question)

pool.package()
