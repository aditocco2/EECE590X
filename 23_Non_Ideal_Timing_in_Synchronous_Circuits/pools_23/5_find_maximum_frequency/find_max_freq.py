import d2l
import image_utils.image_utils as img

pool = d2l.QuestionPool("Find Maximum Frequency")

variants = [
    {"name": "E", "setup": 4, "hold": 2, "c2q": 5, "xor": 2, "not": 1},
    {"name": "F", "setup": 2, "hold": 2, "c2q": 4, "xor": 1, "not": 2},
    {"name": "G", "setup": 5, "hold": 1, "c2q": 6, "xor": 1, "not": 2},
    {"name": "H", "setup": 3, "hold": 4, "c2q": 5, "xor": 3, "not": 1}
]

for i in variants:

    letter, setup, hold, c2q, xor_delay, not_delay = \
        i["name"], i["setup"], i["hold"], i["c2q"], i["xor"], i["not"]

    min_period_ns = max(xor_delay, not_delay) + setup + c2q
    max_freq_MHz = 1000 / min_period_ns


    max_freq_formatted = f"{max_freq_MHz:.1f}"

    dff_label = f"Setup time: {setup} ns\n" + \
    f"Hold time: {hold} ns\n" + \
    f"Clock-to-Q Delay: {c2q} ns"

    xor_label, not_label = f"{xor_delay} ns", f"{not_delay} ns"

    labels = [dff_label, xor_label, not_label]
    # Corresponding coords
    coords = [(243, 657), (479, 129), (479, 277)]

    # Make the picture
    img.apply_labels("circ_23__base2.png", f"circ_23_{letter}.png", labels, coords)

    q_text = "<p>Find the maximum clock frequency in MHz at which " \
    "the non-ideal FSM circuit above will still function correctly. <b>Round to 1 decimal place.</b></p>"
    feedback = f"1000 / ({setup} + {c2q} + {max(xor_delay, not_delay)}) = {max_freq_MHz:.1f} MHz"
    image_link = f"/imagepools/quantumbeef/circ_23_{letter}.png"
    regex_ans = rf"^[^0-9]*{max_freq_formatted}[^0-9]*$"

    question = d2l.SAQuestion(q_text)
    question.add_image(image_link)
    question.add_feedback(feedback)

    question.add_answer(regex_ans, is_regex=True)

    pool.add_question(question)

pool.package()

