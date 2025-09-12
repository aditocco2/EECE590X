import d2l
import random
from wave_utils.wave_utils import *
import image_utils.image_utils as iu

pool = d2l.QuestionPool("Examine Timing Diagram", "examine.csv")

for variant in ["A", "B", "C", "D"]:

    # Ideal circuit variant
    if variant == "A":
        not_delay = 0
        and_delay = 0
    # Non-ideal circuit variants
    else:
        # Random delays from 1 through 5
        not_delay = random.choice(range(1, 6))
        and_delay = random.choice(range(1, 6))

    # Correct delay for the answer
    propagation_delay = not_delay + and_delay

    # Make random signals and put them through the gates (A and not B)
    A = make_random_signal(20)
    B = make_random_signal(20)  
    not_B = wavedrom_gate("not", B, delay=not_delay)
    F = wavedrom_gate("and", A, not_B, delay=and_delay)

    sig_names = ["A", "B", "not_B", "F"]
    gen_sigs = [A, B, not_B, F]

    # Make the pictures
    svg_filename = f"examine_{variant}.svg"
    png_filename = f"examine_{variant}.svg"

    make_wavedrom_image(f"Topic 13 Question 6 (variant {variant})", 
                        sig_names, gen_sigs, out_filename=svg_filename)
    
    iu.svg2png(svg_filename, png_filename)

    # Question setup
    q_text = "<p>The timing diagram above represents the expression <b>ab'</b>. "\
            "Based on the diagram, which of the following is true about the circuit?</p>"
    
    # Correct for variant A
    ans1 = f"The circuit is ideal and has no delays"
    # Correct for other variants
    ans2 = f"The circuit is non-ideal and has a critical path delay of {propagation_delay} ns" 
    # Distractors
    ans3 = f"The circuit is non-ideal and has a critical path delay of {and_delay} ns"
    ans4 = f"The circuit is ideal and has a critical path delay of {propagation_delay} ns"

    question = d2l.MCQuestion(q_text)

    question.add_image(f"/imagepools/quantumbeef/examine_{variant}.png")

    if variant == "A":
        question.add_answer(ans1, 100)
        question.add_answer(ans2, 0)
        question.add_answer(ans3, 0)
        question.add_answer(ans4, 0)
    else:
        question.add_answer(ans1, 0)
        question.add_answer(ans2, 100)
        question.add_answer(ans3, 0)
        question.add_answer(ans4, 0)

    pool.add_question(question)

pool.package()