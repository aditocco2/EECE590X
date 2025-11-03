import d2l
import random
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

image_link = "/imagepools/quantumbeef/composite_24_4.png"

clk = wu.make_clock(18, 8, 4)
          # clk = 000011110000111100
a = wu.to_dotted("000111111111111111")
b = wu.to_dotted("0000xxxxxxx1111111")
c = wu.to_dotted("000000000000xx1111")

wu.make_wavedrom_image("", ["clk", "a", "b", "c"], [clk, a, b, c], out_filename="wave.svg")
img.svg2png("wave.svg", "wave.png", dpi=200)
img.upscale("with_2_ff.png", "with_2_ff_upscaled.png", 2)
img.image_concat(["with_2_ff_upscaled.png", "wave.png"], "composite_24_4.png", "v", cleanup=True)

q_text = f"<p>Suppose that instead of a single FF, a two-FF synchronizer was added to the input, \
        creating the new waveforms shown. \
        Which choice most accurately describes the output <i>Q</i> with this design? </p> "

correct = [
    ("The signal Q will now go to the correct state without glitches", True),
    ("The signal Q is now synchronized and stable", True),
    ("The signal Q will not become unstable in this case", True)
]

wrong = [
    ("The signal Q will never become unstable", False),
    ("The signal Q will still suffer glitches because b caused a setup time violation", False),
    ("The signal Q will still suffer glitches because a did not settle quickly enough", False),
    ("The signal Q has a high likelihood of going into the incorrect state", False),
    ("The signal Q will not suffer from glitches, but it will be in the incorrect state", False)
]

pool = d2l.QuestionPool("2 FF Synchronization")

for _ in range(8):

    choices = random.sample(correct, 1) + random.sample(wrong, 3)

    question = d2l.MCQuestion(q_text)
    question.add_image(image_link)

    for choice in choices:
        answer = choice[0]
        points = 100 if choice[1] else 0
        question.add_answer(answer, points)
    
    pool.add_question(question)

pool.package()