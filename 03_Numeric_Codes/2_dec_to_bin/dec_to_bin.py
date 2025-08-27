#!/bin/python -B
import d2l
import random

pool = d2l.QuestionPool(
        "dec_to_bin",
        "mypool.csv"
        )

number_questions = 50

for val in random.sample(range(0, 256), number_questions):
    bin_val = bin(val)
    bin_val = bin_val[2:]
    ans = bin_val.zfill(8)
    ans_rx = "(?i)(0b)?" + ans

    question_text=f"<p>Write {val}<sub>10</sub> as an 8 bit binary value</p>"
    question = d2l.SAQuestion( question_text )
    question.add_answer(ans_rx, is_regex = True)
    question.add_feedback(ans)

    pool.add_question(question)

pool.dump()
pool.package()
