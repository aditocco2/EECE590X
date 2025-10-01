import wave_utils.wave_utils as wu
import d2l
import random

pool = d2l.QuestionPool("DFF WaveDrom", "dff.csv")

for i in range(50):

    period = random.choice([4, 6, 8])

    D = wu.make_random_signal(20)
    C = wu.make_clock(20, period, 2)

    Q = wu.wavedrom_d_flip_flop(C, D)

    regex_ans = wu.to_regex("Q", Q)


    q_link = wu.make_wavedrom_link("DFF Timing Diagram", ["D", "C"],
                                   [D, C], ["Q"])
    q_link_alt = wu.to_alternate(q_link)
    
    a_link = wu.make_wavedrom_link("DFF Timing Diagram Answer", ["D", "C", "Q"],
                                   [D, C, Q], [])
    a_link_alt = wu.to_alternate(a_link)
    
    q_text = f"<p>In the circuit above, the signal C toggles every {period//2} ns. \
        Click on the link below to open the problem in WaveDrom. \
        Complete the timing diagram, and then paste all your code \
        into the answer box.</p>" \
        f"<p>{q_link}</p>" \
        f"<p>{q_link_alt}</p>"
    
    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/dff.png")
    question.add_answer(regex_ans, is_regex = True)

    question.add_hint('Your wave for F should have 20 characters and look \
                      something like "xxx11100011100011100" (or "x..1..0..1..0..1..0.").')
    
    question.add_feedback(f"<p>Here was the right answer: <p> {a_link} </p><p> {a_link_alt} </p>")

    pool.add_question(question)

pool.package()