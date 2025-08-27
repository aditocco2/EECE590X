#!/bin/python3 -B
import d2l
import random

pool = d2l.QuestionPool(
        "SOP_by_minterms",
        "pool.csv"
        )

choices = [
        "a'b'c'd'",
        "a'b'c'd",
        "a'b'cd'",
        "a'b'cd",
        "a'bc'd'",
        "a'bc'd",
        "a'bcd'",
        "a'bcd",
        "ab'c'd'",
        "ab'c'd",
        "ab'cd'",
        "ab'cd",
        "abc'd'",
        "abc'd",
        "abcd'",
        "abcd"
        ]
        
number_questions = 51

for i in range(number_questions):
    num_minterms = random.randint(3,6)
    f_minterms = random.sample( range(16), num_minterms )
    f_minterms = sorted(f_minterms)
    question_text= f"Which of the following expressions are part of" \
            f" the SOP given by these minterms: m{f_minterms}?"
    question = d2l.MSQuestion( question_text )
    for i in range(16):
        question.add_answer(f"{choices[i]}", is_correct = i in f_minterms  )
    pool.add_question(question)

pool.dump()
pool.package()

