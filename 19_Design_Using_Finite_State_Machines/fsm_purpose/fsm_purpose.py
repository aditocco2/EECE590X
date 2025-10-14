import d2l

pool = d2l.QuestionPool("Describe Behavior/Purpose of FSM")

variants = "ABCD"

q_text = "<p> Suppose input <i>a</i> and output <i>F</i> are a button and LED respectively. \
    What statement best describes the behavior of the FSM above? </p>"

choices = [
    ("A", "<p>Flashes the LED if the button is held down for <i>exactly</i> two clock cycles</p>"),
    ("B", "<p><i>Toggles</i> the LED when the button is pressed</p>"),
    ("C", "<p>Flashes the LED for <i>only one</i> clock cycle, regardless of how long the button is pressed</p>"),
    ("D", "<p>Keeps the LED on when the button is held for <i>3 or more</i> clock cycles</p>")
]

for q_letter in variants:
    image_link = f"/imagepools/quantumbeef/FSM_19_{q_letter}.png"

    question = d2l.MCQuestion(q_text)
    question.add_image(image_link)

    for choice in choices:
        a_letter = choice[0]
        text = choice[1]

        points = 100 if a_letter == q_letter else 0

        question.add_answer(text, points)

    pool.add_question(question)

pool.package()