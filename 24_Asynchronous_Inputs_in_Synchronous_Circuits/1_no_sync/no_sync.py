import d2l
import random
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

image_link = "/imagepools/quantumbeef/composite_24_1.png"

clk = wu.make_clock(18, 8, 4)
          # clk = 000011110000111100
a = wu.to_dotted("000111111111111111")


wu.make_wavedrom_image("", ["clk", "a"], [clk, a], out_filename="wave.svg")
img.svg2png("wave.svg", "wave.png", dpi=200)
img.upscale("no_sync.png", "no_sync_upscaled.png", 2.5)
img.image_concat(["no_sync_upscaled.png", "wave.png"], "composite_24_1.png", "v", cleanup=True)

q_text = f"<p>Suppose the flip-flop above had a setup time of <b>2 ns</b> and the unsynchronized \
    input <i>a</i> changed as shown in the timing diagram. Which of the following choices \
    best describes what would happen to the state Q?</p>"

correct = [
    ("The signal Q will be in an unknown state, which may or may not be correct", True),
    ("The signal Q may or may not enter an incorrect state due to a setup time violation", True),
    ("The signal Q will suffer from glitches before settling to an unpredictable value", True)
]

wrong = [
    ("The signal Q will be forced into the incorrect state due to a setup time violation", False),
    ("The signal Q will stay in the correct state despite the setup time violation", False),
    ("The signal Q will experience glitches at first but settle into the correct state", False),
    ("The signal Q will change state as expected, as there are no violations", False),
    ("The signal Q will be forced into the incorrect state due to a hold time violation", False)
]

pool = d2l.QuestionPool("No Synchronization")

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