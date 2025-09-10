import d2l
import random
from wave_utils.wave_utils import *

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

    
    propagation_delay = not_delay + and_delay

    # Make random signals and put them through the gates (A and not B)
    A = make_random_signal(20)
    B = make_random_signal(20)  
    not_B = wavedrom_gate("not", B, delay=not_delay)
    F = wavedrom_gate("and", A, not_B, delay=and_delay)

    sig_names = ["A", "B", "not_B", "F"]
    gen_sigs = [A, B, not_B, F]


    file = f"examine_{variant}.svg"

    make_wavedrom_image(f"Topic 13 Question 6 (variant {variant})", 
                        sig_names, gen_sigs, out_filename=file)
    
    # Which of the following is true
    # 1 this is ideal with no delays
    # 2 this is non ideal with a delay of (correct)
    # 3 this is ideal with (shortest path (distractor))
    # 4 this is ideal with (correct delay)



