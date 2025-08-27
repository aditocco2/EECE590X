import d2l
import random

pool = d2l.QuestionPool("Absorption using commutative property MAT", "pool.csv")

number_questions = 50


for i in range(number_questions):
    or1 = {"b + abc" : "b",
           "b + a'bc" : "b",
           "b + abc'" : "b",
           "b' + ab'c" : "b'",
           "b' + a'b'c" : "b'",
           "b' + ab'c'" : "b'",
           "c + abc" : "c",
           "c + a'bc" : "c",
           "c + ab'c" : "c",
           "c' + abc'" : "c'",
           "c' + a'bc'" : "c'",
           "c' + ab'c'" : "c'"}
    and1 = {"b(a + b + c)" : "b",
            "b(a' + b + c)" : "b",
            "b(a + b + c')" : "b",
            "b'(a + b' + c)" : "b'",
            "b'(a' + b' + c)" : "b'",
            "b'(a + b' + c')" : "b'",
            "c(a + b + c)" : "c",
            "c(a' + b + c)" : "c",
            "c(a + b' + c)" : "c",
            "c'(a + b + c')" : "c'",
            "c'(a' + b + c')" : "c'",
            "c'(a + b' + c')" : "c'"}
    or2 = {"b + ab'c" : "b + ac",
           "b + a'b'c" : "b + a'c",
           "b' + abc" : "b' + ac",
           "b' + a'bc" : "b' + a'c",
           "c + abc'" : "c + ab",
           "c + a'bc'" : "c + a'b",
           "c' + abc" : "c' + ab",
           "c' + a'bc" : "c' + a'b"} # maybe add a third and fourth for a and b each, that
                                    # look like b + a'b'c' = b + a'c'
    and2 = {"b(a + b' + c)" : "b(a + c)",
            "b(a' + b' + c)" : "b(a' + c)",
            "b'(a + b + c)" : "b'(a + c)",
            "b'(a' + b + c)" : "b'(a' + c)",
            "c(a + b + c')" : "c(a + b)",
            "c(a' + b + c')" : "c(a' + b)",
            "c'(a + b + c)" : "c'(a + b)",
            "c'(a' + b + c)" : "c'(a' + b)"}
    
    match_list = [random.choice(list(or1)), random.choice(list(and1)),
                  random.choice(list(or2)), random.choice(list(and2))]
    

    choice_list = [or1[match_list[0]], and1[match_list[1]],
                   or2[match_list[2]], and2[match_list[3]]]
    
    question_text = "Match each of the following expressions with its reduced form."


    question = d2l.MQuestion(question_text, shuffle = True)

    question.add_answer("", "a")
    question.add_answer("", "a'")
    question.add_answer("", "b")
    question.add_answer("", "b'")
    question.add_answer("", "c")
    question.add_answer("", "c'")
    '''
    question.add_answer("", "b + b'c") 
    question.add_answer("", "a + b'c")
    question.add_answer("", "b' + bc")###just added this
    question.add_answer("", "c + bc'")
    question.add_answer("", "a + bc'")
    '''
    dist_or2 = random.sample(list(or2), 2)
    dist_and2 = random.sample(list(and2), 2)

    for k in range(2):
        question.add_answer("", or2[dist_or2[k]])
        question.add_answer("", and2[dist_and2[k]])
    for j in range(4):
        question.add_answer(match_list[j], choice_list[j])

    pool.add_question(question)

pool.dump()
pool.package()
