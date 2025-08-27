#!/bin/python -B
import d2l
import random

pool = d2l.QuestionPool(
        "binary_not_gate",
        "mypool.csv"
        )

number_questions = 50

for i in range(number_questions):
    val = random.randint(0,256)

    bin_val = bin(val)

    bin_val = bin_val[2:]
    bin_val = bin_val.zfill(8)

    not_out = val ^ 0xFF
    bin_out = bin(not_out)
    ans = bin_out[2:]
    ans = ans.zfill(8)
    ans_rx = "(?i)(0b)?" + ans
    question_text=f"What is the result of NOT {bin_val} in binary?" \
            " Enter your solution as 8 bits without spaces."
    question = d2l.SAQuestion( question_text )
    question.add_answer(ans_rx, is_regex=True)
    question.add_feedback(ans)

    pool.add_question(question)

pool.dump()
pool.package()
