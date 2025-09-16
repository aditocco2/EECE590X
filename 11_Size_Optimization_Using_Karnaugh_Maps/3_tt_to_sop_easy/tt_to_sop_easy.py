import d2l
import random
from html_tt import html_tt
from html_kmap import html_kmap

pool = d2l.QuestionPool("Truth Table to SOP (easy), SA", "pool.csv")

expressions = {'11101000' : ["b'c'", "a'b'", "a'c'"],
               '11010100' : ["b'c", "a'b'", "a'c"],
               '10110010' : ["bc'", "a'b", "a'c'"],
               '01110001' : ['bc', "a'b", "a'c"],
               '10001110' : ["b'c'", "ab'", "ac'"],
               '01001101' : ["b'c", "ab'", 'ac'],
               '00101011' : ["bc'", 'ab', "ac'"],
               '00010111' : ['bc', 'ab', 'ac'],
               '11101100' : ["b'", "a'c'"],
               '10110011' : ['b', "a'c'"],
               '11111000' : ["a'", "b'c'"],
               '10001111' : ['a', "b'c'"],
               '11101010' : ["c'", "a'b'"],
               '11010101' : ['c', "a'b'"],
               '11011100' : ["b'", "a'c"],
               '01110011' : ['b', "a'c"],
               '11110100' : ["a'", "b'c"],
               '01001111' : ['a', "b'c"],
               '10111010' : ["c'", "a'b"],
               '01110101' : ['c', "a'b"],
               '11001110' : ["b'", "ac'"],
               '00111011' : ['b', "ac'"],
               '11110010' : ["a'", "bc'"],
               '00101111' : ['a', "bc'"],
               '10101110' : ["c'", "ab'"],
               '01011101' : ['c', "ab'"],
               '11001101' : ["b'", 'ac'],
               '00110111' : ['b', 'ac'],
               '11110001' : ["a'", 'bc'],
               '00011111' : ['a', 'bc'],
               '10101011' : ["c'", 'ab'],
               '01010111' : ['c', 'ab']}
for exp in list(expressions):
    truth_table = html_tt(exp, ["a", "b", "c", "f"])
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
