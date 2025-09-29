import d2l

pool = d2l.QuestionPool("Determine When The Output Changes")

for period in [20, 30, 40]:
    q_text = f"In the circuit above, the input D changes at 0 ns. \
                The control signal C goes from low to high at 10 ns \
                and toggles every {period//2} ns after that. \
                At what time will the change in D reflect on the output?"

    question = d2l.SAQuestion(q_text)
    question.add_image("/imagepools/quantumbeef/double_dff.png")

    ans = 10 + period
    regex_ans = f"^\\s*({ans})\\s*(ns)*\\s*$"
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{ans} ns")

    pool.add_question(question)

pool.package()