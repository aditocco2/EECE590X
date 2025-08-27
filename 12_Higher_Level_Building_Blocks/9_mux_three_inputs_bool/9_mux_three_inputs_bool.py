import d2l
import random
from DrawWithInputs import *

pool = d2l.QuestionPool( "mux_three_input_bool", "pool.csv" )
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
num_minterms = 3
max_val = 8

for i in range(number_questions):
    f_minterms = random.sample( range(max_val), num_minterms )
    list_terms = [product_term[i] for i in f_minterms]
    canonical_sop = " + ".join(list_terms)
    image = muxBoxDraw(num_minterms, sel="abc", o=canonical_sop)
    
    assign = "a=>s2, b=>s1, c=>s0"
    question_text= "<p>An <b>8-to-1 multiplexer</b> has " \
        f"three select inputs ({assign}). Assume you want " \
        "the multiplexer output to be equivalent to the" \
        " following expression: </p><p> Out = " \
        f"{canonical_sop}</p> <p> Thus, your digital " \
        f"circuit would look as follows: </p> {image} <p>" \
        "What values should be connected to the data inputs?" \
        " Please enter the 8 bits without spaces.</p>"
    question = d2l.SAQuestion( question_text )
    
    ans = ""
    for i in range(max_val):
        added_bit = '1' if i in f_minterms else '0'
        ans = added_bit + ans
    inv_ans = ans[::-1]
    
    question.add_answer(f"(?i)^\s*(0b)?0*{ans}|{inv_ans}\s*$", is_regex = True)
    question.add_feedback(f"{inv_ans}")
    pool.add_question(question)

pool.dump()
pool.package()