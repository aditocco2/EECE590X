import d2l
import random
from DrawWithInputs import *

pool = d2l.QuestionPool( "four_input_decoder_in_out, SA", "pool.csv" )

size = 4
max_val = 2**size

for num_in in range(0, max_val):
    bin_in = bin(num_in)[2:].zfill(size)
    dec = decoderDraw(size, s=bin_in)
    question_text = f"<p>For the following decoder, which output(s):" \
        f" are high? <br> {dec}</p>"
    bin_out = ""
    for i in range(max_val):
        if num_in == i:
            bin_out = '1' + bin_out
        else:
            bin_out = '0' + bin_out
    question = d2l.MSQuestion(question_text)
    # question.add_answer(f"(?i)^\s*(0b)?0*{bin_out}\s*$", is_regex = True)
    for i in range(max_val):
        question.add_answer(f"Out{i}", is_correct = i == num_in  )
    pool.add_question(question)
    
    dec = decoderDraw(size, s="abcd", out_ind=num_in)
    question_text = "<p>What is the binary input, abcd, for the following : " \
        f"decoder? {dec}</p>"
    question = d2l.MSQuestion(question_text)
    # question.add_answer(f"(?i)^\s*(0b)?0*{bin_in}\s*$", is_regex = True)
    for i in range(max_val):
        option = bin(i)[2:].zfill(size)
        question.add_answer(f"abcd: {option}", is_correct = i == num_in  )
    pool.add_question(question)

pool.dump()
pool.package()
