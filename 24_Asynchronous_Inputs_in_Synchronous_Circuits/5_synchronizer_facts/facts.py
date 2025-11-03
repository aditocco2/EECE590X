import d2l
import random

q_text = f"Which of the following are true about two-flip-flop synchronizers \
    as opposed to one-flip-flop synchronizers? Select all that apply."

correct = [
    ("2-FF synchronizers are more glitch-resistant at the cost of more delay", True),
    ("2-FF synchronizers make glitches more unlikely, but even better protection can be achieved with more FFs", True),
    ("2-FF synchronizers make metastability extremely unlikely", True)
]

wrong = [
    ("2-FF synchronizers offer more protection without any additional delay", False),
    ("2-FF synchronizers offer perfect protection, so adding extra FFs does not help", False),
    ("2-FF synchronizers don't make glitches any more unlikely, so they just add delay", False),
    ("2-FF synchronizers offer more protection while speeding up the circuit's operation", False),
    ("2-FF synchronizers have less delay, but are more prone to metastability", False)
]

pool = d2l.QuestionPool("2-FF Synchronizer Facts")

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
