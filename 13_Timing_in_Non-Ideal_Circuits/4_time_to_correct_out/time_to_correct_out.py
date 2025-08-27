import d2l

pool = d2l.QuestionPool("Time to correct output, SA", "pool.csv")

question_text = f"<p>Assume that inputs <i>a</i> and <i>b</i> " \
        f"both change at 0ns, and remain constant afterwards. At" \
        f" what time will the output of F be correct?</p>"

question = d2l.SAQuestion(question_text)
feedback = "Consider how long it takes both signals to" \
        "propogate through the entire circuit"

question.add_answer(f"^\\s*(5)\\s*(ns)*\\s*$", is_regex = True)
question.add_feedback(feedback)
pool.add_question(question)

pool.dump()
pool.package()

