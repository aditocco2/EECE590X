import d2l
import random
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

image_link = "/imagepools/quantumbeef/composite_24_2.png"

clk = wu.make_clock(18, 8, 4)
          # clk = 000011110000111100
a = wu.to_dotted("000111111111111111")
c = wu.to_dotted("0000xxxxx111111111")
D = wu.to_dotted("000000xxxxx111")
Q = wu.to_dotted("000000000000")

wu.make_wavedrom_image("", ["clk", "a", "c", "D", "Q"], [clk, a, c, D, Q], out_filename="wave.svg")
img.svg2png("wave.svg", "wave.png", dpi=200)
img.upscale("with_1_ff.png", "with_1_ff_upscaled.png", 2.5)
img.image_concat(["with_1_ff_upscaled.png", "wave.png"], "composite_24_2.png", "v", cleanup=True)

q_text = f"<p>Suppose a single flip-flop was added in front of this non-ideal FSM. The output of this FF \
    experiences glitches for <b>5 ns</b> before settling into 1, creating the partial waveforms for <i>D</i> \
    and <i>Q</i> shown above. (Each FF still has a setup time of 2 ns).</p> \
    <p>What will happen to the state now? </p>"

correct = [
    ("The signal Q will be unknown because there is a setup time violation in D", True),
    ("The signal Q will become unpredictable because c took too long to settle", True),
    ("The signal Q is no longer guaranteed to be in the correct state", True)
]

wrong = [
    ("The signal Q will stay stable because c settled before the setup time window", False),
    ("The signal Q will stay stable because there is still a transition on c from 0 to 1", False),
    ("The signal Q will suffer from glitches, but eventually settle into the correct state", False),
    ("The signal Q will stay stable because there are no setup time violations in c", False),
    ("The signal Q will suffer from glitches, then be forced into the incorrect state", False)
]

pool = d2l.QuestionPool("1 FF Synchronization (Bad Case)")

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