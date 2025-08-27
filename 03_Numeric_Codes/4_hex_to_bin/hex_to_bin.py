

import d2l
import random


pool = d2l.QuestionPool( "Convert hex to binary, SA", "pool.csv" )

number_questions = 50

for i in range(number_questions):
    decimal_number = random.randint(0, 4069)
    question_text = f"Convert the hexadecimal value {decimal_number:x} " \
            f"into base 2 (binary)."
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"(?i)^\s*(0b)?0*{decimal_number:b}\s*$", is_regex = True)
    question.add_feedback(f"{decimal_number:b}")
    pool.add_question(question)

pool.dump()
pool.package()


