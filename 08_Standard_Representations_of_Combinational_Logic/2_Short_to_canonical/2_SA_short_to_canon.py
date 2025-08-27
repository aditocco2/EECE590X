#!/bin/python3 -B
import d2l
import random

pool = d2l.QuestionPool(
        "short_form_to_canonical_SOP",
        "pool.csv"
        )

question_term = ["a", "a'", "b", "b'", "c", "c'"]
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

number_questions = 50
numQs = 0
while numQs<number_questions:
    qlist1 = random.sample(question_term, 2)
    qlist2 = random.sample(question_term, 2)
    qlist = qlist1 + qlist2
    q_expr = f"{qlist1[0]}{qlist1[1]} + {qlist2[0]}{qlist2[1]}"

    # Lists for answer tracking
    ans_list = []

    # Allocating applicable terms given random question
    for product in product_term:
        qt = list(product.find(qlist[i]) for i in range(len(qlist)))
        for i in range(len(qt)):
            if qlist[i].find("'") < 0:
                if qt[i]+1 < len(product) and product[qt[i]+1] == "'":
                    qt[i] = -1

        if qt[0] >= 0 and qt[1] >=0 and qt[0]!=qt[1]:
            ans_list.append(product)
        elif qt[2] >= 0 and qt[3] >=0 and qt[2]!=qt[3]:
            ans_list.append(product)
    
    ans = "|".join(ans_list)
    fb = " + ".join(ans_list)
    regex_ans = "^"
    
    for i in range(len(ans_list)-1):
        regex_ans += f"\\s*({ans})(?!.*\\{i+1}(?:\\s|\\+|$))\\s*\\+"
    regex_ans += f"\\s*({ans})\\s*$"
    
    if len(ans_list):
        numQs+=1
        question_text= f"<p>Enter the canonical Sum of Products " \
                f"expression that is equivalent to the expression " \
                f"{q_expr}?<br/> NOTE: Enter each term in standard " \
                "(alphabetical) form - i.e. abc + [...]"
        question = d2l.SAQuestion( question_text )
        question.add_answer(f"{regex_ans}", is_regex = True)
        question.add_feedback(f"{fb}")
        pool.add_question(question)

pool.dump()
pool.package()

