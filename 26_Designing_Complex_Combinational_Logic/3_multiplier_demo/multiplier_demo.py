# Testing scripting with external HTML designer (wordtohtml.net)

import d2l

pool = d2l.QuestionPool("Combinational Multiplier Design")

with open("yapping.html", "r") as f:
    q_text_base = f.read()

for bit_length in [2, 4, 6, 8, 12, 16]:

    q_text = q_text_base.replace("[REPLACE]", str(bit_length))

    ans = bit_length - 1
    regex_ans = rf"^\s*{ans}\s*$"
    feedback = f"{ans} adders, as you will have {bit_length} partial products"

    question = d2l.SAQuestion(q_text)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(feedback)

    pool.add_question(question)

pool.package()