import d2l
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

def main():

    pool = d2l.QuestionPool("Non-Ideal FSM Timing Diagram")

    # This question is kind of pointless if there is unknown output from violations,
    # So make signals that have none
    a_signals = [
        #000001111100000111110000011111 <- clk
        "000000001111111111000000000001",
        "100000000111111111101111111100"
    ]
    # Setup time + gate delay cannot exceed 4
    # Hold time cannot exceed 3

    clk = wu.make_clock(30)

    variants = [
        {"name": "A", "setup": 2, "hold": 2, "c2q": 4, "gate": 1},
        {"name": "B", "setup": 2, "hold": 2, "c2q": 3, "gate": 2},
        {"name": "C", "setup": 3, "hold": 1, "c2q": 3, "gate": 1},
        {"name": "D", "setup": 1, "hold": 1, "c2q": 4, "gate": 2}
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

            D, Q = get_D_and_Q(a, gate_delay, c2q, clk)

            # print("D = " + D)
            # print("Q = " + Q)

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
            hint ='<p>Your wave for Q should have 30 characters and look \
                    something like "000001111111111000000000011111".</p>'
            feedback = f"<p>Here was the right answer: {a_link}</p>"

            image_link = f"/imagepools/quantumbeef/circ_23_{letter}.png"

            question = d2l.SAQuestion(q_text)
            question.add_hint(hint)
            question.add_feedback(feedback)
            question.add_image(image_link)
            question.add_answer(regex_ans, is_regex=True)

            pool.add_question(question)

    pool.package()

def get_D_and_Q(a, gate_delay, c2q, clk):

    D = ""
    Q = ""

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
            Q += "0" # starts in state 0

        # Setup and hold time don't matter here 
        # because there are no violations in this problem

    return D, Q
    
if __name__ == "__main__":
    main()