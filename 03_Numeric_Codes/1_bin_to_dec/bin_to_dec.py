#!/bin/python -B
import d2l
import random

pool = d2l.QuestionPool(
        "bin_to_dec",
        "mypool.csv"
        )

number_questions = 50

for val in random.sample(range(17,256), number_questions):
    bin_val = bin(val)
    bin_val = bin_val[2:]
    ans = bin_val.zfill(8)

    question_text=f"Write the binary number {ans} as a decimal value."
    question = d2l.SAQuestion( question_text )
    question.add_answer(f"{val}")
    question.add_feedback(f"{val}")
    pool.add_question(question)

pool.dump()
pool.package()
