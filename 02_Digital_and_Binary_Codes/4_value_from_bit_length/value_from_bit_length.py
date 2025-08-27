#!/bin/python -B
import d2l
import random

pool = d2l.QuestionPool(
        "values_from_bit_length",
        "mypool.csv"
        )

for num_bits in range(0,17):
    ans=2**num_bits 
    question_text="<p>How many <i>unique values</i> can be expressed using binary " +\
            f"encoding with {num_bits} bits?</p>"
    question = d2l.SAQuestion( question_text )
    question.add_answer(str(ans))
    question.add_feedback(str(ans))

    pool.add_question(question)

pool.dump()
pool.package()
