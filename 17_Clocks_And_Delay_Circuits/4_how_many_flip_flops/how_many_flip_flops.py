import d2l
import random

pool = d2l.QuestionPool("How Many Flip Flops")

# Frequencies from 20 to 500 MHz where the period is an integer of ns
frequencies = [i for i in range(20, 501) if 1000/i == int(1000/i)]

for i in range(20):

    frequency_MHz = random.choice(frequencies)
    period_ns = 1000 // frequency_MHz
    flop_count = random.randint(4, 10)
    delay_ns = period_ns * flop_count

    q_text = f"If the clock signal was {frequency_MHz} MHz, and you wanted to \
            see what the value of a signal was {delay_ns} ns ago, how many \
            flip-flops would you need to chain together?"

    ans = flop_count
    # Start of string, any space, ans, anything non-numeric,
    # any space, end of string
    # Stuff that will pass: "8", "8 flip-flops", "8 of them"
    regex_ans = f"^\\s*{ans}\\s*[^0-9]*\\s*$"

    question = d2l.SAQuestion(q_text)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{ans} flip-flops")

    pool.add_question(question)

pool.package()