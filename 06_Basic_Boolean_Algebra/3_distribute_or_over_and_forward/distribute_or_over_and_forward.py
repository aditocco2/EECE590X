#!/bin/python3
import random
import re
import d2l
theorem1 = "{X}+{Y}{Z}=({X}+{Y})({X}+{Z})"

pool = d2l.QuestionPool("Distribute over AND","distribute_and.csv")

def use_vwxyz(expr):
    for l in "abcde":
        expr = expr.replace(l,chr(ord(l)+21))
    return expr

def use_abcde(expr):
    return expr

for i in range(50):
    question = d2l.MQuestion("Match each expression on the left with the" 
                             " expression on the right that is logically equivalent.", shuffle=True)
    encode = random.choice([use_abcde,use_vwxyz])
    inputs = ["a","b","c","d","e"]
    random.shuffle(inputs)
    a, b, c = inputs[0:3]
    lhs1, rhs1 = theorem1.format(X=a,Y=b,Z=c).split("=")
    lhs2, rhs2 = theorem1.format(X=b,Y=a,Z=c).split("=")
    lhs3, rhs3 = theorem1.format(X=c,Y=b,Z=a).split("=")
    for l in "abcde":
        if random.choice([True, False]):
            lhs1 = lhs1.replace(l,l+"'")
            lhs2 = lhs2.replace(l,l+"'")
            lhs3 = lhs3.replace(l,l+"'")
            rhs1 = rhs1.replace(l,l+"'")
            rhs2 = rhs2.replace(l,l+"'")
            rhs3 = rhs3.replace(l,l+"'")
    question.add_answer(encode(lhs1), encode(rhs1))
    question.add_answer(encode(lhs2), encode(rhs2))
    question.add_answer(encode(lhs3), encode(rhs3))

    lhs1, rhs1 = theorem1.format(X=a,Y=b,Z=c).split("=")
    lhs2, rhs2 = theorem1.format(X=b,Y=a,Z=c).split("=")
    lhs3, rhs3 = theorem1.format(X=c,Y=b,Z=a).split("=")
    for l in "abcde":
        if random.choice([True, False]):
            lhs1 = lhs1.replace(l,l+"'")
            lhs2 = lhs2.replace(l,l+"'")
            lhs3 = lhs3.replace(l,l+"'")
            rhs1 = rhs1.replace(l,l+"'")
            rhs2 = rhs2.replace(l,l+"'")
            rhs3 = rhs3.replace(l,l+"'")
    question.add_answer(encode(rhs1), encode(lhs1))
    question.add_answer(encode(rhs2), encode(lhs2))
    question.add_answer(encode(rhs3), encode(lhs3))
    pool.add_question(question)
pool.dump()
pool.package()


    


