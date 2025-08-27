import d2l
import random

pool = d2l.QuestionPool( "mux_num_in_sel, SA", "pool.csv" )

for sel in range(2, 17):
    question_text = "How many input bits does a mux with " \
        f"{sel} select bits have?"
    num_in = 2**sel
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"{num_in}")
    question.add_feedback(f"{num_in}")
    pool.add_question(question)
    
    question_text = "How many select bits does a mux with " \
        f"{num_in} input bits have?"
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"{sel}")
    question.add_feedback(f"{sel}")
    pool.add_question(question)

pool.dump()
pool.package()
