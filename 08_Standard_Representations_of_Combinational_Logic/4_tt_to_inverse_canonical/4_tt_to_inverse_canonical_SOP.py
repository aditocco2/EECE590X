#!/bin/python3 -B
import d2l
import random
from html_tt import html_tt

pool = d2l.QuestionPool(
        "truth_table_to_inverse_canonical_SOP",
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
    val = random.randint(1,255)
    bin_val = bin(val)[2:].zfill(8)
    tt = html_tt(bin_val, ["a", "b", "c", "F"])

    num_terms = bin_val.count('1')
    can = ""
    inv = ""
    distract1 = ""
    distract2 = ""

    list_ans = []
    list_inv = []
    
    for i in range(len(bin_val)):
        if bin_val[i] == '1':
            list_ans.append(product_term[i])
            can+=product_term[i] + " + "
            if i%2==0:
                distract1 += product_term[i] + " + "
            else:
                distract2 += product_term[i] + " + "
        else:
            list_inv.append(product_term[i])
            inv += product_term[i] + " + "
            if i%2==0:
                distract2 += product_term[i] + " + "
            else:
                distract1 += product_term[i] + " + "

    ans = can[:-3]
    wrong1 = inv[:-3]
    wrong2 = distract1[:-3]
    wrong3 = distract2[:-3]

    if wrong2 == ans:
        wrong2 += list_inv[-1]
    elif wrong2 == inv:
        wrong2 = list_ans[0] + wrong2

    if wrong3 == ans:
        wrong3 = list_inv[0] + wrong3
    elif wrong3 == inv:
        wrong3 += list_ans[-1]

    question_text= "<p>Which of the following is the canonical SOP " \
            "expression for the inverse of the function given in " \
            f"the truth table below {tt}? </p>"
    question = d2l.MCQuestion( question_text )
    
    question.add_answer(f"{ans}", 0)
    question.add_answer(f"{wrong1}", 100)
    question.add_answer(f"{wrong2}", 0)
    question.add_answer(f"{wrong3}", 0)

    pool.add_question(question)

pool.dump()
pool.package()

