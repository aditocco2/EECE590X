

import d2l
import random


pool = d2l.QuestionPool( "Convert dec to hex, SA", "pool.csv" )

number_questions = 50

for i in range(number_questions):
    decimal_number = random.randint(0, 4069)
    question_text = f"Convert the decimal number {decimal_number} " \
            f"into hexadecimal (base 16)."
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"(?i)^\s*(0x)?0*{decimal_number:x}\s*$", is_regex = True)
    question.add_feedback(f"{decimal_number:x}")
    pool.add_question(question)

pool.dump()
pool.package()


