import d2l
import random
from html_tt import html_tt
from html_kmap import html_kmap

pool = d2l.QuestionPool("Converting a Truth Table to a Karnaugh Map",
                        "mypool.csv")

number_questions = 50

i = 0

while i < number_questions:
    bin_string = f"{random.choice(range(32768,65536)):016b}"
    
    if (bin_string[12:16] == bin_string[8:12]) or ((bin_string[3] == bin_string[2]) and
                                                   (bin_string[7] == bin_string[6]) and
                                                   (bin_string[11] == bin_string[10]) and
                                                   (bin_string[15] == bin_string[14])):
        continue
    
    truth_table = html_tt(bin_string, ["A", "B", "C", "D", "F"])
  
    correct_kmap = html_kmap(bin_string)

    incorrect_cols = bin_string[:2] + bin_string[3] + bin_string[2] + bin_string[4:6] + bin_string[7] + bin_string[6] + bin_string[8:10] + bin_string[11] + bin_string[10] + bin_string[12:14] + bin_string[15] + bin_string[14]
    
    incorrect_rows = bin_string[0:8] + bin_string[12:16] + bin_string[8:12]
    
    incorrect_cols_rows = bin_string[:2] + bin_string[3] + bin_string[2] + bin_string[4:6] + bin_string[7] + bin_string[6] + bin_string[12:14] + bin_string[15] + bin_string[14] + bin_string[8:10] + bin_string[11] + bin_string[10]
   
    i += 1
    question_text = f"<p>An engineer has been given the following truth " \
            f"table for the circuit F. {truth_table} If the engineer" \
            f" wanted to optimize the circuit using a Karnaugh Map, " \
            f"which of the following would be the correctly filled out map?</p>"
            
    
    question = d2l.MCQuestion(question_text)
    
    question.add_answer(correct_kmap, 100)
    question.add_answer(html_kmap(f"{incorrect_rows}"), 0)
    question.add_answer(html_kmap(f"{incorrect_cols}"), 0)
    question.add_answer(html_kmap(f"{incorrect_cols_rows}"), 0)
    
    pool.add_question(question)

pool.dump()
pool.package()


