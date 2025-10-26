import d2l
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

pool = d2l.QuestionPool("Non-Ideal DFF Timing Diagram")

variants = [
    {"name": "A", "setup": 4, "hold": 2, "c2q": 5},
    {"name": "B", "setup": 2, "hold": 2, "c2q": 4},
    {"name": "C", "setup": 5, "hold": 1, "c2q": 6},
    {"name": "D", "setup": 3, "hold": 4, "c2q": 5}
]

for i in variants:

    letter, setup, hold, c2q = i["name"], i["setup"], i["hold"], i["c2q"]

    label = f"Setup time: {setup} ns\n" + \
    f"Hold time: {hold} ns\n" + \
    f"Clock-to-Q Delay: {c2q} ns"

    coords = (320, 360)

    img.apply_labels("dff_23__base.png", f"dff_23_{letter}.png", [label], [coords], 40)


    # 40 variants total
    for _ in range(10):

        clk = wu.make_clock(30)
        D = wu.make_random_signal(30, 3)
        Q = wu.wavedrom_d_flip_flop(clk, D, setup_time=setup, hold_time=hold, delay=c2q)

        q_link = wu.make_wavedrom_link("Non-Ideal DFF Diagram", ["clk", "D"],
                                       [clk, D], ["Q"])

        a_link = wu.make_wavedrom_link("Non-Ideal DFF Diagram Answer", ["clk", "D", "Q"],
                                       [clk, D, Q], [])

        regex_ans = wu.to_regex("Q", Q)

        q_text = f"<p>In this problem, the flip-flop is <i>not</i> ideal and has  \
        the delays shown above. \
        Click on the link below to open the problem in WaveDrom. Complete the timing \
        diagram, and paste <b>all</b> your code into the answer box.</p> \
        <p>{q_link}</p>"
        hint = 'Your wave for Q should have 30 characters and look \
                something like "xxxxxxxxxx11111111110000000000".'
        feedback = f"<p>Here was the right answer: {a_link}</p>"

        image_link = f"/imagepools/quantumbeef/dff_23_{letter}.png"

        question = d2l.SAQuestion(q_text)
        question.add_hint(hint)
        question.add_feedback(feedback)
        question.add_image(image_link)
        question.add_answer(regex_ans, is_regex=True)

        pool.add_question(question)

pool.package()