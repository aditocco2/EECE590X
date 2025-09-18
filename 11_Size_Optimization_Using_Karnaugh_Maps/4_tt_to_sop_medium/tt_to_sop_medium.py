import d2l
import random
from html_tt import html_tt
from html_kmap import html_kmap

pool = d2l.QuestionPool("Truth Table to SOP (medium), SA", "q11_q4.csv")

expressions = {"1100111111111100": ["c'","a'b","ab'"],
               "1111111101000001": ["a'","bcd","b'c'd"],
               "1100110100110111": ["a'c'","bd","ac"],
               "1111000110010011": ["a'b'","cd","abc","b'c'd'"],
               "1000111100010011": ["a'c'd'","a'b","bc","acd"],
               "0111010111011111": ["d","ab","ac'","a'b'c"],
               "1101110111110010": ["a'c'","a'd","ab'","acd'"]}

for exp in list(expressions):
    truth_table = html_tt(exp, ["a", "b", "c", "d", "f"])
    question_text = f"<p>Given the following truth table for " +\
            "the circuit f, use a Karnaugh Map to find the " +\
            "simplified SOP (sum of products) expression for f." +\
            f"{truth_table}</p>"
    
    question = d2l.SAQuestion(question_text)

    ans = "|".join(expressions[exp])
    regex_ans = "^"
    feedback_ans = "+".join(expressions[exp])

    for i in range(len(expressions[exp])-1):
        regex_ans += f"\\s*({ans})(?!.*\\{i+1}[^'a-z])\\s*\\+"
    regex_ans += f"\\s*({ans})\\s*$"

    question.add_answer(f"{regex_ans}", is_regex = True)
    question.add_feedback(f"{feedback_ans}")

    pool.add_question(question)

pool.dump()
pool.package()
    
