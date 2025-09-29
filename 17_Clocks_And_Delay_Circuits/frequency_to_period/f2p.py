import d2l
import random

pool = d2l.QuestionPool("Frequency to Period")

# This one does not use sigfigs and instead relies on period being a whole number.
# May change to sigfigs later.

# Frequency from 2 to 500 MHz, where the period is a whole number of nanoseconds
frequencies = [i for i in range(2, 501) if 1000/i == int(1000/i)]

for frequency_MHz in frequencies:

    period_ns = 1000/frequency_MHz

    q_text = f"A clock signal has a frequency of {frequency_MHz} MHz. \
               How many nanoseconds will elapse between the clock's rising edges?"
    question = d2l.SAQuestion(q_text)

    ans = int(period_ns)
    regex_ans = f"^\\s*({ans})\\s*(ns)*\\s*$"
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{ans} ns")

    pool.add_question(question)

pool.package()