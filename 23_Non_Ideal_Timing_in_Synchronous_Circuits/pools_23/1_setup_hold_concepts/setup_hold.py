import d2l

pool = d2l.QuestionPool("Setup and Hold Time Concepts")

variants = [
    ("<p> The <i>setup</i> time of a flip-flop is the amount of time " +
    "<i>before</i> the rising edge of the clock that the inputs must remain stable.</p>", True),

    ("<p> The <i>setup</i> time of a flip-flop is the amount of time " +
    "<i>after</i> the rising edge of the clock that the inputs must remain stable.</p>", False),

    ("<p> The <i>hold</i> time of a flip-flop is the amount of time " +
    "<i>before</i> the rising edge of the clock that the inputs must remain stable.</p>", False),

    ("<p> The <i>hold</i> time of a flip-flop is the amount of time " +
    "<i>after</i> the rising edge of the clock that the inputs must remain stable.</p>", True),

    ("<p> The clock-to-Q delay is the propagation delay " +
    "of the logic <i>inside</i> the flip-flop.", True),

    ("<p> The clock-to-Q delay is the propagation delay " +
    "of the logic <i>outside</i> the flip-flop.", False)
]

for v in variants:

    q_text = v[0]
    ans = v[1]

    question = d2l.TFQuestion(q_text, points=5)
    question.add_answer(ans)

    pool.add_question(question)
    
pool.package()
