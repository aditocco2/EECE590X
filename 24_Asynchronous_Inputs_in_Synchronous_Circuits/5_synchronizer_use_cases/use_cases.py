import d2l
import random

q_text = f"In which of the following scenarios would a synchronizer be necessary? Select all that apply."

correct = [
    ("A signal coming from a different system with a different clock frequency", True),
    ("A signal coming from a different system with the same clock frequency", True),
    ("A system sampling an external waveform at an unknown frequency", True),
    ("A switch on the FPGA board", True),
    ("A button on the FPGA board", True),
]

wrong = [
    ("An input from a circuit that is running on the same clock as the rest of the system", False),
    ("An internal signal going from one register to another in the same system, assuming a shared clock", False),
    ("A signal going directly to the LEDs on the FPGA board", False),
    ("A signal going into a purely combinational circuit", False)
]

pool = d2l.QuestionPool("Synchronizer Use Cases")

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
