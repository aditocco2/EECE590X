import d2l
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

pool = d2l.QuestionPool("Determine Circuit Type from Timing Diagram")

q_text = "Based on the timing diagram above, what do A and B represent?"

for variant in ["A", "B", "C", "D", "E", "F"]:

    answer_choices = {
        "The two inputs to an AND gate": 0,
        "The S and R inputs of an SR latch, respectively": 0,
        "The D and E inputs of a D latch, respectively": 0,
    }

    # Variants A and B are the combinational circuit (AND gate)
    if variant in ["A", "B"]:
        A = wu.make_random_signal(20, 5)
        B = wu.make_random_signal(20, 5)
        C = wu.wavedrom_gate("and", A, B)
        answer_choices["The two inputs to an AND gate"] = 100

    # Variants C and D are the SR latch
    elif variant in ["C", "D"]:
        while True:
            try:
                A = wu.make_random_signal(20, 6)
                B = wu.make_random_signal(20, 6)
                C = wu.wavedrom_sr_latch(A, B)
                break
            except:
                pass
        answer_choices["The S and R inputs of an SR latch, respectively"] = 100

    # Variants E and F are the D latch
    else:
        while True:
            try:
                A = wu.make_random_signal(20, 6)
                B = wu.make_random_signal(20, 4)
                C = wu.wavedrom_d_latch(A, B)
                break
            except:
                pass
        answer_choices["The D and E inputs of a D latch, respectively"] = 100

    image_name = f"unknown_diagram_15{variant}"

    wu.make_wavedrom_image("Timing Diagram", ["A", "B", "C"],
                           [A, B, C], [], f"{image_name}.svg")
    
    img.svg2png(f"{image_name}.svg", f"{image_name}.png")

    question = d2l.MCQuestion(q_text, shuffle=False)

    question.add_image(f"/imagepools/quantumbeef/{image_name}.png")

    for ans in answer_choices.keys():
        points = answer_choices[ans]
        question.add_answer(ans, points)

    pool.add_question(question)

pool.package()