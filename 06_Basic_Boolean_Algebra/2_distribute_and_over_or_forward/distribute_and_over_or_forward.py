#!/bin/python3
import random
import re
import d2l
theorem1 = "{X}({Y}+{Z})={X}{Y}+{X}{Z}"

literal = lambda x : x
inverse = lambda x : x+"'"

pool = d2l.QuestionPool("Distribute over OR","distribute_or.csv")

def use_vwxyz(expr):
    for l in "abcde":
        expr = expr.replace(l,chr(ord(l)+21))
    return expr
def use_abcde(expr):
    return expr
    
def order_literals(expr):
    terms = expr.split("+")
    return  "+".join(["".join(sorted(re.findall(r".'?",t))) for t in terms])

for i in range(50):
    question = d2l.MQuestion("Match each expression on the left with the" 
                             " expression on the right that is logically equivalent.")
    inputs = ["a","b","c","d","e"]
    encode = random.choice([use_abcde,use_vwxyz])
    random.shuffle(inputs)
    inputs = "".join(inputs)
    splits = sorted(random.sample(range(1,6),3))
    terms=["".join(sorted(inputs[0:splits[0]])), 
           "".join(sorted(inputs[splits[0]:splits[1]])), 
           "".join(sorted(inputs[splits[1]:splits[2]])) ]
    a, b, c = terms
    lhs1, rhs1 = theorem1.format(X=a,Y=b,Z=c).split("=")
    lhs2, rhs2 = theorem1.format(X=b,Y=a,Z=c).split("=")
    lhs3, rhs3 = theorem1.format(X=c,Y=b,Z=a).split("=")
    rhs1 = order_literals(rhs1)
    rhs2 = order_literals(rhs2)
    rhs3 = order_literals(rhs3)
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
    rhs1 = order_literals(rhs1)
    rhs2 = order_literals(rhs2)
    rhs3 = order_literals(rhs3)
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
