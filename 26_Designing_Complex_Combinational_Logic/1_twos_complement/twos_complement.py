import d2l
import random

pool = d2l.QuestionPool("Two's Complement Representation")

# Decimal to two's complement

numbers = random.sample(range(-128, 1), 20)

for num in numbers:
    q_text = f"<p>What is the 8-bit two's complement representation \
        of the decimal number {num}? </b>"
    
    twos = f"{(num & 0xFF):8b}" # two's complement binary string
    regex_ans = rf"^\s*{twos}\s*$"

    question = d2l.SAQuestion(q_text)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{twos}")
    pool.add_question(question)

# Two's complement to decimal

numbers = random.sample(range(-128, 1), 20)

for num in numbers:

    twos = f"{(num & 0xFF):8b}"

    q_text = f"<p>What is the decimal representation of the \
        signed binary number {twos} (in two's complement)? </b>"
    
    regex_ans = rf"^\s*{num}\s*$"

    question = d2l.SAQuestion(q_text)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{num}")
    pool.add_question(question)

pool.package()