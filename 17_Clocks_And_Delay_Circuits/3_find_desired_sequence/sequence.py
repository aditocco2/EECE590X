import d2l
import random
import image_utils.image_utils as im
import os

pool = d2l.QuestionPool("Find Sequence for Shift Register Thingy")

q_text = "Suppose the input D in the above circuit is a sequence of 1s and 0s being sent \
    at the same rate as the clock frequency. What sequence would make the output Q go high?"

# Coords go from right FF to left FF because right FF shows older input
all_coords = [(1115, 267), (895, 267), (703, 267), (508, 267), (310, 267)]

# Get some random 5 bit sequences in binary
numbers = random.sample(range(32), 5)
sequences = [f"{number:05b}" for number in numbers]

# Clean up old images before regenerating new ones
for filename in os.listdir("."):
    if filename.startswith("sequence") and filename.endswith("png") \
                                        and "11111" not in filename:
        os.remove(filename)

# 5 variants
for sequence in sequences:

    # Create a new list of not gate coords corresponding to where the sequence has 0s
    coords_to_paste = [all_coords[i] for i in range(len(all_coords)) if sequence[i] == "0"]

    # Paste the NOT gates where they need to go and save the new image
    in_filename = "sequence_11111.png"
    out_filename = f"sequence_{sequence}.png"
    im.paste_images(in_filename, out_filename, "NOT_vertical.png", coords_to_paste, 0.5)

    regex_ans = f"^\\s*{sequence}\\s*$"

    question = d2l.SAQuestion(q_text)
    question.add_image(f"/imagepools/quantumbeef/{out_filename}")
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(sequence)

    pool.add_question(question)

pool.package()