#!/bin/python3 -B
import d2l
import random

pool = d2l.QuestionPool(
        "Select_minterm_from_Canonical_SOP",
        "pool.csv"
        )

product_term = [
        "a'b'c'",
        "a'b'c",
        "a'bc'",
        "a'bc",
        "ab'c'",
        "ab'c",
        "abc'",
        "abc"
        ]
        
number_questions = 51

for i in range(number_questions):
    num_minterms = random.randint(2,4)
    f_minterms = random.sample( range(8), num_minterms )
    canonical_sop = " + ".join( [product_term[i] for i in f_minterms ] )
    question_text= f"Which of the following are minterms of the" \
            f" expression: {canonical_sop}?"
    question = d2l.MSQuestion( question_text )
    for i in range(8):
        question.add_answer(f"<p>m<sub>{i}</sub></p>", is_correct = i in f_minterms  )
    pool.add_question(question)

pool.dump()
pool.package()

