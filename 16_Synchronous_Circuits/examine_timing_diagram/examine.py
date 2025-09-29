import d2l
import random
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

pool = d2l.QuestionPool("Determine Memory Unit from Timing Diagram")

q_text = "What kind of memory unit is shown in the timing diagram above? \
        Assume A and B are the inputs and C is the output."

for variant in ["A", "B", "C", "D", "E", "F"]:

    # One of these will be given 100 points later
    answer_choices = {
        "An SR-latch": 0,
        "A D-latch": 0,
        "A D Flip-Flop": 0
    }

    # Variants A and B are the SR latch
    if variant in ["A", "B"]:
        while True:
            try:
                A = wu.make_random_signal(20, 6)
                B = wu.make_random_signal(20, 6)
                C = wu.wavedrom_sr_latch(A, B)
                break
            except:
                pass
        answer_choices["An SR-latch"] = 100

    # Variants C and D are the D latch
    elif variant in ["C", "D"]:
        while True:
            try:
                A = wu.make_random_signal(20, 6)
                B = wu.make_random_signal(20, 4)
                C = wu.wavedrom_d_latch(A, B)
                break
            except:
                pass
        answer_choices["A D-latch"] = 100

    # Variants E and F are the flip-flop
    else:
        A = wu.make_random_signal(20, 6)
        B = wu.make_clock(20, 8, 6) # Want some high clock time at the start
        C = wu.wavedrom_d_flip_flop(B, A)
        answer_choices["A D Flip-Flop"] = 100

    image_name = f"unknown_diagram_16{variant}"

    wu.make_wavedrom_image("Timing Diagram", ["A", "B", "C"],
                           [A, B, C], [], f"{image_name}.svg")
    
    img.svg2png(f"{image_name}.svg", f"{image_name}.png")
    print(f"Made image {variant}")

    question = d2l.MCQuestion(q_text, shuffle=False)

    question.add_image(f"/imagepools/quantumbeef/{image_name}.png")

    for ans in answer_choices.keys():
        points = answer_choices[ans]
        question.add_answer(ans, points)

    pool.add_question(question)

pool.package()