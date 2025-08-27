import d2l

pool = d2l.QuestionPool("Critical Path", "pool.csv")

question_text = f'<p>What is the <b>critical path delay</b> of the <b>non-ideal</b> circuit.</p>'
question = d2l.SAQuestion(question_text)
feedback = "Consider the longest possible path."

question.add_answer(f"^\\s*(5)\\s*(ns)*\\s*$", is_regex = True)
question.add_feedback(feedback)
pool.add_question(question)

pool.dump()
pool.package()


