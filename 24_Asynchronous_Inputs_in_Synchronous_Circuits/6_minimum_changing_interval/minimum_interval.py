import d2l
import random

pool = d2l.QuestionPool("Minimum Changing Interval of Input")

image_link = "/imagepools/quantumbeef/synch.png"

# Whole frequencies from 5 to 500 MHz where the period is a whole number
freqs = [i for i in range(5, 501) if 1000/i == 1000//i]

for freq in freqs:
    q_text = f"<p> Suppose a system is designed where the asynchronous input \
        <i>A</i> shown above goes through a 2-FF synchronizer, and the result \
        <i>S</i> is used throughout the rest of the system.</p> \
        <p>The clock frequency is <b>{freq}</b> MHz. What is the minimum time interval \
        in <b>nanoseconds</b> at which A should be allowed to change?</p>"
    
    # Double The clock period
    min_interval = (1000 // freq) * 2

    # start of string, any space, ans, any space, anything non numeric,
    # end of string
    regex_ans = f"^\\s*{min_interval}\\s*[^0-9]*\\s*$"

    question = d2l.SAQuestion(q_text)
    question.add_image(image_link)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{min_interval} ns")

    pool.add_question(question)

pool.package()


    
