import d2l
import random


pool = d2l.QuestionPool( "Convert hex to decimal, SA", "mypool.csv" )

number_questions = 50

for i in range(number_questions):
    decimal_number = random.randint(0, 4069)
    question_text = f"Convert the hexadecimal value {decimal_number:x} " \
            f"into base 10 (decimal)."
    question = d2l.SAQuestion(question_text)
    question.add_answer(f"^\s*{decimal_number}\s*$", is_regex = True)
    question.add_feedback(f"{decimal_number}")    
    pool.add_question(question)

pool.dump()
pool.package()


