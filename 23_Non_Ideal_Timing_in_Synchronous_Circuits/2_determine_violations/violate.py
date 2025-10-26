import d2l
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

pool = d2l.QuestionPool("Determine Setup/Hold Time Violations")

clk = wu.make_clock(30)

setup, hold, c2q = 3, 2, 5

variants = [
    # No violations
    # clk: 000001111100000111110000011111
    ("A", "100000000111111111101111111100"),
    ("B", "000000001111111111000000000001"),

    # Setup time violation only
    # clk: 000001111100000111110000011111
    ("C", "000011111111100000011110000000"),
    ("D", "111000000001110000001111000000"),

    # Hold time violation only
    # clk: 000001111100000111110000011111
    ("E", "000000111110000011110111110000"),
    ("F", "100000100000000011111111110101"),

    # Both violations
    # clk: 000001111100000111110000011111
    ("G", "000111000000000011111111000000"),
    ("H", "111100000000000011111111001111"),
]

choices = [
    "<p>The output will be predictable</p>",
    "<p>The output will be unpredictable because of <i>setup time</i> violations only</p>",
    "<p>The output will be unpredictable because of <i>hold time</i> violations only</p>",
    "<p>The output will be unpredictable because of <i>both setup and hold time</i> violations</p>"
]

q_text = f"<p>Suppose the <i>clk</i> and <i>D</i> inputs above go into a \
    non-ideal flip-flop with a setup time of <b>{setup} ns</b>, a hold time \
    of <b>{hold} ns</b>, and a clock-to-Q delay of <b>{c2q} ns</b>. \
    What can be said about the output of this flip-flop?</p>"

for i in range(len(variants)):

    letter, signal = variants[i][0], variants[i][1]
    ans = choices[i//2] # A and B get choice 0, etc.

    image_name = f"diagram_23_{letter}"
    image_link = f"/imagepools/quantumbeef/{image_name}.png"

    signal = wu.to_dotted(signal)
    wu.make_wavedrom_image("Question 2 Timing Diagram", ["clk", "D"],
                           [clk, signal], [], f"{image_name}.svg")
    
    img.svg2png(f"{image_name}.svg", f"{image_name}.png")

    question = d2l.MCQuestion(q_text, shuffle=False)
    question.add_image(image_link)

    for choice in choices:
        points = 100 if ans == choice else 0
        question.add_answer(choice, points)

    pool.add_question(question)

pool.package()



    
