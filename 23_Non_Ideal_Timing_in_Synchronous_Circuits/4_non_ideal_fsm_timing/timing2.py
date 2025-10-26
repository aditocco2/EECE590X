import d2l
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

pool = d2l.QuestionPool("Non-Ideal FSM Timing Diagram")

# This question is kind of pointless if there is unknown output from violations,
# So make signals that have none
a_signals = [
    "000000001111111111000000000001",
    "100000000111111111101111111100"
]

clk = wu.make_clock(30)

variants = [
    {"name": "A", "setup": 4, "hold": 2, "c2q": 5, "gate": 1},
    {"name": "B", "setup": 2, "hold": 2, "c2q": 4, "gate": 2},
    {"name": "C", "setup": 5, "hold": 1, "c2q": 6, "gate": 3},
    {"name": "D", "setup": 3, "hold": 4, "c2q": 5, "gate": 2}
]

for i in variants:

    letter, setup, hold, c2q, gate_delay = i["name"], i["setup"], i["hold"], i["c2q"], i["gate"]

    dff_label = f"Setup time: {setup} ns\n" + \
    f"Hold time: {hold} ns\n" + \
    f"Clock-to-Q Delay: {c2q} ns"

    gate_label = f"{gate_delay} ns"

    gate_coords = (152, 236)
    dff_coords = (418, 454)

    labels = [gate_label, dff_label]
    coords = [gate_coords, dff_coords]

    img.apply_labels("circ_23__base.png", f"circ_23_{letter}.png", labels, coords, 40)

    # 8 variants total
    for a in a_signals:

        # wait, how am I gonna do feedback
        # uhh

        D = ""
        Q = "" # initial value

        for i in range(30):

            # extract D[i] from Q[i] and a[i]
            if i >= gate_delay:
                D += wu.wavedrom_gate("xor", a[i-gate_delay], Q[i-gate_delay])
            else:
                D += "x"
            
            # FF logic to get Q
            if i >= c2q:
                if clk[i-c2q] == "1":
                    Q += D[i-c2q]
                else:
                    Q += Q[i-1]
            else:
                Q += "0"

            # Setup and hold time don't matter here

        D = wu.to_dotted(D)
        Q = wu.to_dotted(Q)

        q_link = wu.make_wavedrom_link("Non-Ideal FSM Circuit Timing Diagram", ["clk", "a"],
                                        [clk, a], ["D", "Q"])

        a_link = wu.make_wavedrom_link("Non-Ideal FSM Circuit Timing Diagram Answer", ["clk", "a", "D", "Q"],
                                        [clk, a, D, Q], [])

        regex_ans = wu.to_regex("Q", Q)

        q_text = f"<p>The circuit above is a simple FSM with a <i>non-ideal</i> gate and \
        flip-flop. Their delays and other attributes are shown above.</p> \
        <p><b>Assume the FSM starts in state 0.</b></p> \
        Click on the link below to open the problem in WaveDrom. Complete the timing \
        diagram, and paste <b>all</b> your code into the answer box.</p> \
        <p>{q_link}</p>"
        hint = 'Your wave for Q should have 30 characters and look \
                something like "000001111111111000000000011111".'
        feedback = f"<p>Here was the right answer: {a_link}</p>"

        image_link = f"/imagepools/quantumbeef/circ_23_{letter}.png"

        question = d2l.SAQuestion(q_text)
        question.add_hint(hint)
        question.add_feedback(feedback)
        question.add_image(image_link)
        question.add_answer(regex_ans, is_regex=True)

        pool.add_question(question)

pool.package()