import d2l
import random
from DrawWithInputs import *

pool = d2l.QuestionPool( "three_input_mux", "pool.csv" )

size = 4
max_val = 2**size
max_ins = 2**max_val

for num_in in range(0, max_val):
    bin_in = bin(num_in)[2:].zfill(size)
    ins = random.randint(0, max_ins-1)
    ins_bin = bin(ins)[2:].zfill(max_val)
    dec = muxBoxDraw(size, sel=bin_in, ins = ins_bin)
    question_text = f"<p>What is the output for the following mux? " \
        f"<br> {dec}</p>"
    an = ins_bin[len(ins_bin)-1-num_in]
    question = d2l.MCQuestion(question_text)
    # question.add_answer(f"(?i)^\s*(0b)?0*{bin_out}\s*$", is_regex = True)
    for i in ['1', '0']:
        question.add_answer(f"{i}", (100 if i == an else 0))
    pool.add_question(question)
    
    dec = muxBoxDraw(size, ins=ins_bin, o=an)
    question_text = "<p>What are the possible select input signals, " \
        f"abc, for the following mux? {dec}</p>"
    question = d2l.MSQuestion(question_text)
    # question.add_answer(f"(?i)^\s*(0b)?0*{bin_in}\s*$", is_regex = True)
    for i in range(max_val):
        option = bin(i)[2:].zfill(size)
        question.add_answer(f"{option}", is_correct = (True if ins_bin[len(ins_bin)-1-i] == an else False))
    pool.add_question(question)

pool.dump()
pool.package()