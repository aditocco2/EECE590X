#!/bin/python3
import random
import re
import d2l

literal = lambda x : x
inverse = lambda x : x+"'"

qtext= "<p> Write a Boolean expression that is equivalent to {exp} which does not use parenthesis.</p>"

regex1 = r"^\s*a\s*\+\s*(?:bcd|bdc|cbd|cdb|dbc|dcb)\s*$"
regex2 = r"^\s*(?:bcd|bdc|cbd|cdb|dbc|dcb)\s*\+\s*a\s*$"

pool = d2l.QuestionPool("Extend Distributive Or","mixed_extend_distribute_or.csv")

for num_questions in range(25):
    a,b,c,d = random.sample("vwxyz",4)
    expr = random.choice([ 
                          f"({a}+{b})({a}+{c})({a}+{d})",
                          f"({a}+{b})({a}+{c})({d}+{a})",
                          f"({a}+{b})({c}+{a})({a}+{d})",
                          f"({a}+{b})({c}+{a})({d}+{a})",
                          f"({b}+{a})({a}+{c})({a}+{d})",
                          f"({b}+{a})({a}+{c})({d}+{a})",
                          f"({b}+{a})({c}+{a})({a}+{d})",
                          f"({b}+{a})({c}+{a})({d}+{a})" ]
                         )
    ans1 = regex1.replace("a",a).replace("b",b).replace("c",c).replace("d",d)
    ans2 = regex2.replace("a",a).replace("b",b).replace("c",c).replace("d",d)
    for l in "vwxyz":
        if random.choice([True, False]):
            expr = expr.replace(l,l+"'")
            ans1 = ans1.replace(l,l+"'")
            ans2 = ans2.replace(l,l+"'")

    question=d2l.SAQuestion(qtext.format(exp=expr))
    question.add_answer(ans1,100,is_regex=True)
    question.add_answer(ans2,100,is_regex=True)
    pool.add_question(question)

pool.dump()
pool.package()
