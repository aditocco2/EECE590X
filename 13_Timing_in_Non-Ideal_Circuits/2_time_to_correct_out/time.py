import d2l
from image_utils.image_utils import *

pool = d2l.QuestionPool("Time to correct output", "pool.csv")

question_text = f"<p>Assume that inputs A, B, C, and D above " \
        f"all change at 0 ns and remain constant afterwards. At" \
        f" what time will the output G be correct?</p>"

feedback = "Consider how long it takes all signals to " \
        "propagate through the entire circuit."

variants = [
    {"name": "A", "not_delay": 1, "and_delay": 2, "or_delay": 3},
    {"name": "B", "not_delay": 1, "and_delay": 5, "or_delay": 4},
    {"name": "C", "not_delay": 2, "and_delay": 2, "or_delay": 2},
    {"name": "D", "not_delay": 3, "and_delay": 4, "or_delay": 5},
]

# Coordinates of where to label each gate (from top left)
not_coords = [(350, 160), (350, 460)]
and_coords = [(550, 550), (550, 250)]
or_coords  = [(770, 390)]

for variant in variants:
    coords = not_coords + and_coords + or_coords
    labels = [variant["not_delay"], variant["not_delay"],
              variant["and_delay"], variant["and_delay"],
              variant["or_delay"]]
    labels = [f"{i} ns" for i in labels]

    image_name = "time.png"
    image_copy_name = f"time_{variant["name"]}.png" # time_A.png, etc.

    apply_labels(image_name, image_copy_name, labels, coords)


    ans = variant['not_delay'] + variant['or_delay'] + variant["and_delay"]
    # Start of string, any spaces, answer, any spaces, ns, any spaces, end of string
    regex_ans = f"^\\s*({ans})\\s*(ns)*\\s*$"

    question = d2l.SAQuestion(question_text, 
                              title=f"Time to Correct Output (variant {variant['name']})")

    question.add_image(f"/imagepools/quantumbeef/{image_copy_name}")
    question.add_answer(regex_ans, is_regex = True)
    question.add_feedback(feedback)
    pool.add_question(question)

# pool.dump()
pool.package()

