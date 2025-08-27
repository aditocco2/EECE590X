import d2l
import random

pool = d2l.QuestionPool( "decoder_num_in_out, SA", "pool.csv" )

for num_in in range(2, 17):
    question_text = "How many output bits does a decoder with " \
        f"{num_in} input bits have?"
    num_out = 2**num_in
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"{num_out}")
    question.add_feedback(f"{num_out}")

    pool.add_question(question)
    
    question_text = "How many input bits does a decoder with " \
        f"{num_out} output bits have?"
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"{num_in}")
    question.add_feedback(f"{num_in}")
    pool.add_question(question)

pool.dump()
pool.package()