import d2l

pool_0 = d2l.QuestionPool("SR Latch Reset Behavior", "q14_3.csv")
pool_1 = d2l.QuestionPool("SR Latch Set Behavior", "q14_2.csv")

text_0 = "When do SR latches reset their output to 0?"
answers_0 = [
    ("When R goes low", 0),
    ("When R goes high", 100),
    ("When S goes low", 0),
    ("When S goes high", 0),
]

text_1 = "When do SR latches set their output to 1?"
answers_1 = [
    ("When R goes low", 0),
    ("When R goes high", 0),
    ("When S goes low", 0),
    ("When S goes high", 100)
]

# Half the normal number of points cause these are really simple questions
question_0 = d2l.MCQuestion(text_0, points=5)
for (answer, points) in answers_0:
    question_0.add_answer(answer, points)

question_1 = d2l.MCQuestion(text_1, points=5)
for (answer, points) in answers_1:
    question_1.add_answer(answer, points)

pool_0.add_question(question_0)
pool_0.package()

pool_1.add_question(question_1)
pool_1.package()