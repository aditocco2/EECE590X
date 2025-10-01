import d2l
import wave_utils.wave_utils as wu

pool = d2l.QuestionPool("D Latch Timing Diagram", "d_timing.csv")

for i in range(50):

    # Repeat until valid signals are made to pass through the D latch
    while True:
        try:
            D = wu.make_random_signal(20)
            E = wu.make_random_signal(20)
            # D latch with unknown initial value
            Q = wu.wavedrom_d_latch(D, E)
            break
        except:
            pass

    regex_ans = wu.to_regex("Q", Q)

    q_link = wu.make_wavedrom_link("D Latch Timing Diagram", ["D", "E"],
                                   [D, E], ["Q"])
    q_link_alt = wu.to_alternate(q_link)
    
    a_link = wu.make_wavedrom_link("D Latch Timing Diagram Answer", ["D", "E", "Q"],
                                   [D, E, Q], [])
    a_link_alt = wu.to_alternate(a_link)
    
    q_text = "<p>The image above shows a standard implementation of a D latch. \
        Click on the link below to open the problem in WaveDrom. \
        Complete the timing diagram, and then paste all your code \
        into the answer box.</p>" \
        f"<p>{q_link}</p>" \
        f"<p>{q_link_alt}</p>"

    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/d_latch.png")
    question.add_answer(regex_ans, is_regex = True)

    question.add_hint('Your wave for F should have 20 characters and look \
                      something like "00000111110001110000" (or "0....1....0..1..0..."). \
                      You may or may not have unknown output (x) at the start.')

    question.add_feedback(f"<p>Here was the right answer: <p> {a_link} </p><p> {a_link_alt} </p>")

    pool.add_question(question)

pool.package()