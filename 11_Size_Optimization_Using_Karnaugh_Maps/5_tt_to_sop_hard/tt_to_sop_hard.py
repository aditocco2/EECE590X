import d2l
import random
from html_tt import html_tt
from html_kmap import html_kmap

pool = d2l.QuestionPool("Truth Table to SOP (hard), SA", "q11_q5.csv")

number_questions = 50
expressions = {"1110011110100010" : [["b'd'","cd'","a'bd","a'c'd"],
                                     ["b'd'","cd'","a'bd","a'b'c'"],
                                     ["b'd'","cd'","a'c'd","a'bc"]],
               "0111001101111110" : [["cd'","b'd","a'c","abc'"]],
               "0100101010101010" : [["ad'","bd'","a'b'c'd"]],
               "1000110000110101" : [["a'c'd'","ab'c","a'bc'","abd"],
                                     ["a'c'd'","ab'c","bc'd","acd"],
                                     ["a'c'd'","ab'c","bc'd","abd"]],
               "1001110110010010" : [["a'c'd'","b'c'd'","a'cd","b'cd","abcd'","a'bc'"],
                                     ["a'c'd'","b'c'd'","a'cd","b'cd","abcd'","a'bd"]],
               "0001110101000111" : [["a'bc'","ac'd","abc","a'cd"]],
               "1101011100010100" : [["a'b'c'","bc'd","a'bc","b'cd"]]}

for exp in list(expressions):
    truth_table = html_tt(exp, ["a", "b", "c", "d", "f"])
    question_text = f"<p>Given the following truth table for " \
            "the circuit f, use a Karnaugh Map to find the " \
            "simplified SOP (sum of products) expression for f." \
            f"{truth_table}</p>"
    
    feedback_ans = "+".join(expressions[exp][0])
    question = d2l.SAQuestion(question_text)
    for sop in range(len(expressions[exp])):
        ans = "|".join(expressions[exp][sop])
        regex_ans = "^"

        

        for i in range(len(expressions[exp][sop])-1):
            regex_ans += f"\\s*({ans})(?!.*\\{i+1})\\s*\\+"
        regex_ans += f"\\s*({ans})\\s*$"

        question.add_answer(f"{regex_ans}", is_regex = True)
    question.add_feedback(f"{feedback_ans}")
    pool.add_question(question)

pool.dump()
pool.package()
