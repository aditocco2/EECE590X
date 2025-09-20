import d2l
import wave_utils.wave_utils as wu

pool = d2l.QuestionPool("SR Latch Timing Diagram", "sr_timing.csv")

for i in range(50):

    S = wu.make_random_signal(20)
    R = wu.make_random_signal(20)
    # SR latch assuming initial value is 0
    Q = wu.wavedrom_sr_latch(S, R, 0)

    regex_ans = wu.to_regex("Q", Q)

    q_link = wu.make_wavedrom_link("Topic 14 Question 2", ["S", "R"],
                                   [S, R], ["Q"])
    q_link_alt = wu.to_alternate(q_link)
    
    a_link = wu.make_wavedrom_link("Topic 14 Question 2 Answer", ["S", "R", "Q"],
                                   [S, R, Q], [])
    a_link_alt = wu.to_alternate(a_link)
    
    q_text = "<p>The image above shows a standard implementation of an SR latch. \
        Click on the link below to open the problem in WaveDrom. \
        Complete the timing diagram, and then paste all your code \
        into the answer box.</p>" \
        "<p><b>Assume that the initial value of the signal is 0.<br>" \
        "Assume that if both S and R are high, the latch resets.</b></p>" \
        f"<p>{q_link}</p>" \
        f"<p>{q_link_alt}</p>"

    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/sr_latch.png")
    question.add_answer(regex_ans, is_regex = True)

    question.add_hint('Your wave for Q should have 20 characters and look \
                      something like "0....1....0..1..0..."')

    question.add_feedback(f"<p>Here was the right answer: <p> {a_link} </p><p> {a_link_alt} </p>")

    pool.add_question(question)

pool.package()