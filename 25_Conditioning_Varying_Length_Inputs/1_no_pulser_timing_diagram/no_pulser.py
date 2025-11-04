import d2l
import random
import wave_utils.wave_utils as wu

image_link = "/imagepools/quantumbeef/FSM_25_A.png"

def main():

    pool = d2l.QuestionPool("FSM Without Pulser")

    for _ in range(40):

        clk = wu.make_clock(20, 2, 1)
        b = wu.make_pulses(20, 5, 10, 2, 6)

        F = get_F(b, clk)

        print(clk)
        print(b)
        print(F)

        q_link = wu.make_wavedrom_link("FSM Without Pulser", ["clk", "b"],
                                    [clk, b], ["F"])
        
        a_link = wu.make_wavedrom_link("FSM Without Pulser Answer", ["clk", "b", "F"],
                                    [clk, b, F], [])
        
        q_text = f"<p>The following FSM is designed to toggle the output <i>F</i> continously \
            while a button input <i>b</i> is high.</p> \
            <p><b>Assume the circuit starts in the off state with F=0.<b></p> \
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