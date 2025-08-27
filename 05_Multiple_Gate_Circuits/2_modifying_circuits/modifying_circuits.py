import d2l
import random
from html_tt import html_tt

pool = d2l.QuestionPool( "Modify the given circuit MC", "pool.csv" )

number_questions = 50

i = 0
while i < number_questions:

    F = random.randint(17, 65535)
    G = random.randint(17, 65535)
    
    if (F == G) or (F == ~G&0xffff):
        continue

    i += 1

    F_tt = html_tt(str(f"{F:>016b}"), ["A", "B", "C", "D", "F"])
    G_tt = html_tt(str(f"{G:>016b}"), ["A", "B", "C", "D", "G"])

    FandG = F & G
    ForG = F | G
    notF = ~F & 0xffff
    notG = ~G & 0xffff
 
    type_of_circuit = {
            "F and G" : FandG,
            "F or G" : ForG,
            "not F" : notF,
            "not G" : notG
            }
    correct_choice = random.choice(sorted(type_of_circuit))


    correct_inv = ''.join('1' if x == '0' else '0' for x in
                          f"{type_of_circuit[correct_choice]:>016b}")
    
    correct_tt = html_tt([f"{F:>016b}", f"{G:>016b}",
                         f"{type_of_circuit[correct_choice]:>016b}"], ["A",
                                                                       "B",
                                                                       "C",
                                                                       "D",
                                                                       "F",
                                                                       "G",
                                                                       f"{correct_choice}"])
    correct_inv_tt = html_tt([f"{F:>016b}", f"{G:>016b}",f"{correct_inv}"], ["A",
                                                                       "B",
                                                                       "C",
                                                                       "D",
                                                                       "F",
                                                                       "G",
                                                                       f"{correct_choice}"])
    
    question_text = f"<p>The truth tables for circuits F and G are " \
            f"shown below.</p>{F_tt}{G_tt}<p>Which of the following would be a correct" \
            f" truth table if we were to modify the circuits F and G " \
            f"to produce <b>{correct_choice}</b>?</p>"
    
    question = d2l.MCQuestion(question_text)
    question.add_answer(correct_tt, 100)
    
    question.add_answer(correct_inv_tt, 0)
  
    type_of_circuit.pop(correct_choice)

    other_choice = random.sample(sorted(type_of_circuit), 2)

    
    for x in range(2):
        other_tt = html_tt([f"{F:>016b}", f"{G:>016b}", f"{type_of_circuit[other_choice[x]]:>016b}"], ["A",
                                                                       "B",
                                                                       "C",
                                                                       "D",
                                                                       "F",
                                                                       "G",
                                                                       f"{correct_choice}"])
        question.add_answer(other_tt, 0)
   
    pool.add_question(question)

pool.dump()
pool.package()


