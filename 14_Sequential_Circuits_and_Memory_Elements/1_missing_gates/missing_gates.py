import d2l
import random

pool = d2l.QuestionPool("Fill In Missing Gates", "missing.csv")

q_text = "Suppose you are designing an SR latch from scratch \
          using basic logic gates. Which gates would belong \
          in slots A and B in the diagram above?"


# Setting shuffle=True does a static shuffle of choices, so I gotta make variants
for i in range(40):

    question = d2l.MQuestion(q_text, shuffle=True)

    question.add_image("/imagepools/quantumbeef/sr_latch_missing_gates.png")

    # # First two are correct for gates A and B, others are distractors
    # choices = ["OR", "AND", "XOR", "NOR", "NAND", "XNOR"]

    # random.shuffle(choices)

    # for gate in choices:
    #     if gate == "OR":
    #         question.add_answer("Gate A", gate)
    #     elif gate == "AND":
    #         question.add_answer("Gate B", gate)
    #     else:
    #         question.add_answer(choice=gate)

    # Correct Choices
    question.add_answer("Gate A", "OR")
    question.add_answer("Gate B", "AND")

    # Distractors
    question.add_answer(choice="XOR")
    question.add_answer(choice="NOR")
    question.add_answer(choice="NAND")
    question.add_answer(choice="XNOR")

    pool.add_question(question)

pool.dump()
pool.package()