import d2l
from image_utils.image_utils import *

pool = d2l.QuestionPool("Critical Path", "critical.csv")
question_text = f'<p>What is the <b>critical path delay</b> of the following <b>non-ideal</b> circuit?</p>'
feedback = "Consider the longest possible path."

variants = [
    {"name": "A", "not_delay": 1, "and_delay": 2, "or_delay": 2},
    {"name": "B", "not_delay": 1, "and_delay": 3, "or_delay": 3},
    {"name": "C", "not_delay": 3, "and_delay": 4, "or_delay": 5},
    {"name": "D", "not_delay": 3, "and_delay": 2, "or_delay": 1},
]

# Coordinates of where to label each gate (from top left)
not_coords = [(348, 132), (348, 470)]
and_coords = [(546, 234)]
or_coords  = [(820, 325)]

for variant in variants:

    # Make list of labels/coords
    # Circuit has 2 nots, 1 and, and 1 or
    coords = not_coords + and_coords + or_coords
    labels = [f"{variant['not_delay']} ns", f"{variant['not_delay']} ns", 
              f"{variant['and_delay']} ns", f"{variant['or_delay']} ns"]

    # Make copies of the diagram called "critical_A.png", etc.
    image_name = "critical.png"
    image_copy_name = f"critical_{variant['name']}.png"

    # Add labels
    apply_labels(image_name, image_copy_name, labels, coords)

    ans = variant['not_delay'] + variant['or_delay'] + variant["and_delay"]

    question = d2l.SAQuestion(question_text, title=f"Critical Path (variant {variant['name']})")

    # Start of string, any spaces, answer, any spaces, ns, any spaces, end of string
    regex_ans = f"^\\s*({ans})\\s*(ns)*\\s*$"

    question.add_image(f"/imagepools/quantumbeef/{image_copy_name}")
    question.add_answer(regex_ans, is_regex = True)
    question.add_feedback(feedback)
    pool.add_question(question)

# pool.dump()
pool.package()


