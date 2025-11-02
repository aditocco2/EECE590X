import d2l
import random
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

image_link = "/imagepools/quantumbeef/composite_24_2.png"


clk = wu.make_clock(18, 8, 4)
          # clk = 000011110000111100
a = wu.to_dotted("000111111111111111")
c = wu.to_dotted("0000xxxx0000111111")

wu.make_wavedrom_image("", ["clk", "a", "c"], [clk, a, c], out_filename="wave.svg")
img.svg2png("wave.svg", "wave.png", dpi=200)
img.upscale("with_1_ff.png", "with_1_ff_upscaled.png", 2.5)
img.image_concat(["with_1_ff_upscaled.png", "wave.png"], "composite_24_2.png", "v", cleanup=True)

q_text = f"<p>Suppose a single flip-flop was added in front of this non-ideal FSM. The output of this FF \
    experiences glitches for <b>4 ns</b> before settling back into 0 as shown above. What will \
    happen to the state now? </p>"

correct = [
    ("The signal Q will stay in the correct state because the input c now has a good transition from 0 to 1", True),
    ("The signal Q will stay in the correct state, as the sampling of c does not have violations", True),
    ("The signal Q will stay in the correct state because c settled quickly enough to avoid violations", True)
]

wrong = [
    ("The signal Q will still be forced into the incorrect state because the signal a has violations", False),
    ("The signal Q will still be in an unknown state, which may or may not be correct", False),
    ("The signal Q will still become unstable because the signal c takes too long to settle", False),
    ("The signal Q will suffer from glitches before settling to an unpredictable value",  False),
    ("The signal Q will stay in the correct state regardless of how quickly c settles", False)
]

pool = d2l.QuestionPool("1 FF Synchronization (Good Case)")

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