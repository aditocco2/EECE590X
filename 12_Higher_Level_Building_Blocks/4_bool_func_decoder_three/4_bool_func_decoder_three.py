#!/bin/python3 -B
from three_var_bool_optimization import three_var_bool_optimization

import d2l
import random
from DrawWithInputs import *

pool = d2l.QuestionPool(
        "Boolean_Function_Through_Decoder, MS",
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
    num_minterms = random.randint(3,5)
    f_minterms = random.sample( range(8), num_minterms )
    simplified = three_var_bool_optimization(f_minterms)
    simplified = " + ".join(simplified)
    image = decoderDraw(3, s="abc")
    question_text= "<p>Assume you'd like to implement the followng " \
        "<i>Boolean function</i> with a three-input decoder and an " \
        f"OR gate (not shown):</p><p>F = {simplified}</p><p>If a, b," \
        " and c are connected to i2, i1, and i0 respectively, which of" \
        f" the following decoder outputs should you utilize?</p> {image}"
    question = d2l.MSQuestion( question_text )
    for i in range(8):
        question.add_answer(f"<p>d<sub>{i}</sub></p>", is_correct = i in f_minterms  )
    pool.add_question(question)

pool.dump()
pool.package()

