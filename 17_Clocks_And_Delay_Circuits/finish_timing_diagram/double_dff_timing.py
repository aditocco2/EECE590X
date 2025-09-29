import wave_utils.wave_utils as wu
import d2l
import random

pool = d2l.QuestionPool("Double DFF WaveDrom")

for i in range(50):

    # Keep a short clock period so signals can show up on multiple clock cycles
    period = 4

    D = wu.make_random_signal(20)
    clk = wu.make_clock(20, period, 2)

    F = wu.wavedrom_d_flip_flop(clk, D)
    G = wu.wavedrom_d_flip_flop(clk, F)

    regex_ans = wu.to_regex("G", G)


    q_link = wu.make_wavedrom_link("Double DFF Timing Diagram", ["D", "clk"],
                                   [D, clk], ["F", "G"])
    q_link_alt = wu.to_alternate(q_link)
    
    a_link = wu.make_wavedrom_link("Double DFF Timing Diagram Answer", ["D", "clk", "F", "G"],
                                   [D, clk, F, G], [])
    a_link_alt = wu.to_alternate(a_link)
    
    q_text = f"<p>You have arrived at yet another timing diagram question, \
        this time with two flip-flops. \
        Click on the link below to open the problem in WaveDrom. \
        Complete the timing diagram, and then paste all your code \
        into the answer box.</p>" \
        f"<p>{q_link}</p>" \
        f"<p>{q_link_alt}</p>"
    
    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/double_dff_with_label.png")
    question.add_answer(regex_ans, is_regex = True)

    question.add_hint('Your wave for G should have 20 characters and look \
                      something like "xx1100110000001111110011" (or "x.1.0.1.0.....1.....0.1.").')
    
    question.add_feedback(f"<p>Here was the right answer: <p> {a_link} </p><p> {a_link_alt} </p>")

    pool.add_question(question)

pool.package()