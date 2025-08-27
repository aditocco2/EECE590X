#!/bin/python -B
import d2l
import random

pool = d2l.QuestionPool(
        "decimal_and_gate",
        "mypool.csv"
        )

number_questions = 50

for i in range(number_questions):
    val1 = random.randint(0,256)
    val2 = random.randint(0,256)
    and_out = val1 & val2
    bin_out = bin(and_out)
    ans = bin_out[2:]
    ans = ans.zfill(8)
    ans_rx = "(?i)(0b)?" + ans

    question_text=f"<p>What is the result of {val1}<sub>10</sub> AND {val2}<sub>10</sub> in binary?" \
            " Enter your solution as 8 bits without spaces."
    question = d2l.SAQuestion( question_text )
    question.add_answer(ans_rx, is_regex=True)
    question.add_feedback(ans)
    
    pool.add_question(question)

pool.dump()
pool.package()
