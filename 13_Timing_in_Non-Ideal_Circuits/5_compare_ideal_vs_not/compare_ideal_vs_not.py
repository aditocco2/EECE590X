import d2l

image_name = "ideal_vs_not.png"
# I just added the labels manually for this one ¯\_(ツ)_/¯

pool = d2l.QuestionPool("Compare ideal vs non ideal, MS", "pool.csv")

question_text = f"<p>Analyze the circuit above. " \
        "Which of the following are true about the ideal " \
        "and non-ideal output values of F? <i>Select all " \
        "that apply.</i></p>"

question = d2l.MSQuestion(question_text)

question.add_answer(f"<p>The two outputs are identical, but the" \
                    f" <i>non-ideal</i> output <b>F</b> arrives " \
                    f"<b>5ns later</b>", 
                    is_correct = True)

question.add_answer(f"<p>Whenever <b>more than 5ns</b> has elapsed " \
                    f"since the <i>most recent</i> change in either <i>A</i>" \
                    f" or <i>B</i>, the ideal and non-ideal circuits" \
                    f" will have the same output.</p>",
                    is_correct = True)

question.add_answer(f"This circuit can suffer glitches, which can " \
                    f"persist for <b>longer than 5ns</b> per single glitch.", 
                    is_correct= False)

question.add_answer(f"This circuit can suffer glitches, which " \
                    f"persist for <b><i>no</i> longer than 5ns</b> per single glitch.",
                    is_correct = True)

question.add_image(f"/imagepools/quantumbeef/{image_name}")
pool.add_question(question)

pool.dump()
pool.package()

