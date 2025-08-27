#!/bin/python3

import d2l
import random

pool = d2l.QuestionPool("Develop a code","codings.csv")


        
values = "ABCDEFG"

for i in range(3,7):
    qtext = f"You are designing a digital circuit which can process {i} unique values" \
            f", called Value_A through Value_{values[i-1]}.  Before starting the design," \
             " you must first decide on a method to encode the values. For efficiency," \
             " you should use the fewest number of bits possible to encode the values." \
            f" In the box below, enter a possible encoding for the {i} values: "
    for j in range(i):
        qtext = qtext + f"Value_{values[j]}, "
    qtext = qtext[:-2]
    question = d2l.SAQuestion(qtext)
    bits = 2 if i <= 4 else 3
    match = f"\\W*(\\b[01]{{{bits}}}\\b)"
    answer = match.join(f"(?!.*\\{j})" for j in range(0,i+1))
    answer = "^" + answer[8:-8] + "\\W*$"
    question.add_answer(answer,is_regex=True)
    pool.add_question(question)
pool.dump()
pool.package()
