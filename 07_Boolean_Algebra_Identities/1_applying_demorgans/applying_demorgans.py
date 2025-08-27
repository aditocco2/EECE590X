import d2l
import random

pool = d2l.QuestionPool( "Applying DeMorgan's theorem to F, MC", "pool.csv")

number_questions = 50

for i in range(number_questions):
    
    equations = {"(a+b'+c)(d'+e')"  : "a'bc' + de",
                 "a'bc' + de"       : "(a+b'+c)(d'+e')",
                 "(a'+b+c')(d+e)"   : "ab'c + d'e'",
                 "ab'c + d'e'"      : "(a'+b+c')(d+e)",
                 "(a+b'+c)(d+e)"    : "a'bc' + d'e'",
                 "a'bc' + d'e'"     : "(a+b'+c)(d+e)",
                 "(a'+b+c')(d'+e')" : "ab'c + de",
                 "ab'c + de"        : "(a'+b+c')(d'+e')",
                 "(a'+b'+c')(d+e)"  : "abc + d'e'",
                 "abc + d'e'"       : "(a'+b'+c')(d+e)",
                 "(a+b+c)(d'+e')"   : "a'b'c' + de",
                 "a'b'c' + de"      : "(a+b+c)(d'+e')",
                 "(a+b'+c)(d'+e)"   : "a'bc' + de'",
                 "a'bc' + de'"      : "(a+b'+c)(d'+e)",
                 "(a'+b+c')(d+e')"  : "ab'c + d'e",
                 "ab'c + d'e"       : "(a'+b+c')(d+e')"
                 }
    F = random.choice(sorted(equations))      
    variation = random.choice(range(3))
   
    
    if variation == 0:
        F_original = F
        F = F
    elif variation == 1:
        F_original = F
        F = F.replace("a","v").replace("b","w").replace("c","x").replace("d","y").replace("e","z")
    else:
        F_original = F
        F = F.replace("a","g").replace("b","h").replace("c","i").replace("d","j").replace("e","k")
       
    
    
    for key in equations.keys():
        if variation == 0:
            equations[key] = equations[key]
        elif variation == 1:
            equations[key] = equations[key].replace("a","v").replace("b","w").replace("c", "x").replace("d",
                                                                                                    "y").replace("e",
                                                                                                                 "z")
        else:
            equations[key] = equations[key].replace("a","g").replace("b","h").replace("c", "i").replace("d",
                                                                                                    "j").replace("e",
                                                                                                                 "k")

 
        question_text = f"<p>Which expression is the correct <i>" \
    f"DeMorgan's complement</i> of the function F = {F}? In other " \
    f"words, which expression could be obtained by applying only" \
    f"DeMorgan's theorem to F?</p>"

    question = d2l.MCQuestion(question_text)
    question.add_answer(equations[F_original], 100)
    
    others = random.sample(sorted(equations), 6)
    
    num_distractors = 0
    j = 0
    while num_distractors < 5:
        j += 1
        if equations[F_original] == equations[others[j-1]]:
            continue
        
        num_distractors += 1
        question.add_answer(equations[others[j-1]], 0)        
    pool.add_question(question)
pool.dump()
pool.package()
