import d2l

pool = d2l.QuestionPool("Adding Enable to SR Latch", "sr_enable.csv")

q_text = 'Suppose you want to add an "Enable" (E) signal to an SR \
        latch, where the output Q can only be set or reset if E is \
        high. Would the above diagram be a correct way of implementing \
        this feature?'

for variant in ["A", "B"]:

    question = d2l.MCQuestion(q_text, shuffle=False)

    # Correct implementation variant
    if variant == "A":
        question.add_image("/imagepools/quantumbeef/sr_with_enable_right.png")
        question.add_answer("Yes", 100)
        question.add_answer("No", 0)
    # Wrong implementation variant
    else:
        question.add_image("/imagepools/quantumbeef/sr_with_enable_wrong.png")
        question.add_answer("Yes", 0)
        question.add_answer("No", 100)

    pool.add_question(question)

pool.package()