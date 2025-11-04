import d2l
import random
import os
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

image_link = "/imagepools/quantumbeef/composite_25_2.png"

def main():

    img.upscale("FSM_25_B.png", "upscaled.png", 2)
    img.image_concat(["pulser_25.png", "upscaled.png"], "composite_25_2.png", "v", cleanup=False)
    os.remove("upscaled.png")

    pool = d2l.QuestionPool("FSM With Pulser")

    for _ in range(40):

        clk = wu.make_clock(20, 2, 1)
        b = wu.make_pulses(20, 5, 10, 2, 6, "0")

        # pulser
        b1 = wu.wavedrom_d_flip_flop(clk, b)
        b2 = wu.wavedrom_d_flip_flop(clk, b1)
        not_b2 = wu.wavedrom_gate("not", b2)
        c = wu.wavedrom_gate("and", b1, not_b2)

        F = get_F(c, clk)

        # print(clk)
        # print(wu.to_dotless(b))
        # print(wu.to_dotless(b1))
        # print(wu.to_dotless(b2))
        # print(wu.to_dotless(c))
        # print(wu.to_dotless(F))
        # print("")

        q_link = wu.make_wavedrom_link("FSM With Pulser", ["clk", "b"],
                                    [clk, b], ["b1", "b2", "c", "F"])
        
        a_link = wu.make_wavedrom_link("FSM With Pulser Answer", ["clk", "b", "b1", "b2", "c", "F"],
                                    [clk, b, b1, b2, c, F], [])
        
        q_text = f"<p>Suppose you instead only want the FSM to toggle once when the button \
            <i>b</i> is pressed, so you add a pulser, as shown above.</p> \
            <p><b>Again, assume the circuit starts in the off state with F=0.</b></p> \
            <p>Use the link below to open the \
            problem in WaveDrom. Finish the timing diagram, and then paste <b>all</b> your \
            code into the answer box.</p> \
            <p>{q_link}</p>"
        
        hint = "Your wave should be 20 characters and be comprised of exclusively 1s and 0s."

        feedback = f"<p>Here was the right answer: {a_link}</p>"

        regex_ans = wu.to_regex("F", F)

        question = d2l.SAQuestion(q_text)
        
        question.add_image(image_link)
        question.add_hint(hint)
        question.add_feedback(feedback)
        question.add_answer(regex_ans, is_regex=True)

        pool.add_question(question)

    pool.package()


def get_F(a, clk):
    
    a = wu.to_dotless(a)

    F = ""
    F_value = "0" #initial

    for i in range(len(a)):

        # if A is high right before a clock edge, F toggles
        if clk[i] == "1" and a[i-1] == "1":
            if F_value == "0":
                F_value = "1"
            else:
                F_value = "0"

        F += F_value

    F = wu.to_dotted(F)

    return F
    
if __name__ == "__main__":
    main()