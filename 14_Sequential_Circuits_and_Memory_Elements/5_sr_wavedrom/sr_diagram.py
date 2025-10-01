import d2l
import wave_utils.wave_utils as wu

pool = d2l.QuestionPool("SR Latch Timing Diagram", "sr_timing.csv")

for i in range(50):

    # Repeat until valid signals are made to pass through the SR latch
    while True:
        try:
            S = wu.make_random_signal(20)
            R = wu.make_random_signal(20)
            # SR latch with unknown initial value
            Q = wu.wavedrom_sr_latch(S, R)
            break
        except:
            pass

    regex_ans = wu.to_regex("Q", Q)

    q_link = wu.make_wavedrom_link("SR Latch Timing Diagram", ["S", "R"],
                                   [S, R], ["Q"])
    q_link_alt = wu.to_alternate(q_link)
    
    a_link = wu.make_wavedrom_link("SR Latch Timing Diagram Answer", ["S", "R", "Q"],
                                   [S, R, Q], [])
    a_link_alt = wu.to_alternate(a_link)
    
    q_text = "<p>The image above shows a standard implementation of an SR latch. \
        Click on the link below to open the problem in WaveDrom. \
        Complete the timing diagram, and then paste all your code \
        into the answer box.</p>" \
        f"<p>{q_link}</p>" \
        f"<p>{q_link_alt}</p>"

    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/sr_latch.png")
    question.add_answer(regex_ans, is_regex = True)

    question.add_hint('<p>Your wave for F should have 20 characters and look \
                      something like "00000111110001110000" (or "0....1....0..1..0..."). \
                      You may or may not have unknown output (x) at the start. </p> \
                      <p> You can assume that if S and R are high at the same time, the latch resets.</p>')

    question.add_feedback(f"<p>Here was the right answer: <p> {a_link} </p><p> {a_link_alt} </p>")

    pool.add_question(question)

pool.package()