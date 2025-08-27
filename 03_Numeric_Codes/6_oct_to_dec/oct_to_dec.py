

import d2l
import random


pool = d2l.QuestionPool( "Convert oct to dec SA", "mypool.csv" )

number_questions = 50

for i in range(number_questions):
    decimal_number = random.randint(0, 512)
    question_text = f"<p>What is {decimal_number:o}<sub>8</sub> " \
            f"in decimal?</p>"
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"^\s*{decimal_number}\s*$", is_regex = True)
    question.add_feedback(f"{decimal_number}")    
    pool.add_question(question)

pool.dump()
pool.package()


