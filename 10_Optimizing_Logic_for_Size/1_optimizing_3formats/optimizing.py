import d2l
import random
from html_tt import html_tt 
from string_to_minterms import string_to_minterms
from string_to_som import string_to_som

pool = d2l.QuestionPool("Optimizing without KMaps SA", "pool.csv")

number_questions = 150

expressions = {"11111000" : "b'c' + a'", 
               "11110100" : "b'c + a'",
               "11110010" : "bc' + a'",
               "11110001" : "bc + a'",
               
               "10001111" : "b'c' + a",
               "01001111" : "b'c + a",
               "00101111" : "bc' + a",
               "00011111" : "bc + a",
               
               "11101100" : "a'c' + b'",
               "11011100" : "a'c + b'",
               "11001110" : "ac' + b'",
               "11001101" : "ac + b'",

               "10110011" : "a'c' + b",
               "01110011" : "a'c + b",
               "00111011" : "ac' + b",
               "00110111" : "ac + b",

               "11101010" : "a'b' + c'",
               "10111010" : "a'b + c'",
               "10101110" : "ab' + c'",
               "10101011" : "ab + c'",

               "11010101" : "a'b' + c",
               "01110101" : "a'b + c",
               "01011101" : "ab' + c",
               "01010111" : "ab + c"
               }
for key in expressions.keys():
    format_type = ["truth_table", "expression", "function"]
    for type in format_type:      
        if type == "truth_table":
            formatted_expression = html_tt(key, ["a", "b", "c", "Result"])
            
        elif type == "expression":
            formatted_expression = string_to_som(key)
            formatted_expression = formatted_expression.replace("0",
                                                                "a'b'c'").replace("1",
                                                                                  "a'b'c").replace("2",
                                                                                                   "a'bc'").replace("3",
                                                                                                                    "a'bc").replace("4",
                                                                                                                                    "ab'c'").replace("5", "ab'c").replace("6", "abc'").replace("7", "abc")
            
        else:
            formatted_expression = string_to_minterms(key)
            formatted_expression = f"F(a, b, c) = &#931;m({formatted_expression})" 
 
        question_text = f"<p>Using any method, optimize the {type}" \
                f" below for size. <p>{formatted_expression}</p></p>"
        question = d2l.SAQuestion(question_text)

        answer_terms = expressions[key].split(" + ")

        question.add_answer(f"^\\s*({answer_terms[0]}|{answer_terms[1]})(?!.*\\1[^'a-z])\\s*\\+\\s*({answer_terms[0]}|{answer_terms[1]})\\s*$",
                        is_regex = True)

        question.add_feedback(f"{answer_terms[0]} + {answer_terms[1]}")
        pool.add_question(question)
pool.dump()
pool.package()
