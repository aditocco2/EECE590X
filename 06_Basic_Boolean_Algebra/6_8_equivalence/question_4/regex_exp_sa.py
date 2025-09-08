#!/bin/python -B
import d2l
import random
import string

pool = d2l.QuestionPool(
        "Write boolean expression considering precedence",
        "pool.csv"
        )

q_exp = {
            "(a+b)(c+d')" : "^\s*(ac|ad'|bc|bd')(?!.*\1)\s*\+\s*(ac|ad'|bc|bd')(?!.*\2)\s*\+\s*(ac|ad'|bc|bd')\s*\+\s*(ac|ad'|bc|bd')\s*$" #"ac+ad'+bc+bd'"
        }
# how to fix the backslash escape, \\ doesn't work
for key in q_exp:
    question_text= f"<p>Construct a Boolean expression which has the \
                    same function and <u>precedence</u> as the \
                    expression below:</p>" \
                    + f"<p><b>key</b></p> \
                    <p>Do <u>not</u> include parentheses.</p>"
    question = d2l.SAQuestion( question_text )
    question.add_answer(f"{q_exp[key]}", is_regex=True)
    pool.add_question(question)

pool.dump()
pool.package()
