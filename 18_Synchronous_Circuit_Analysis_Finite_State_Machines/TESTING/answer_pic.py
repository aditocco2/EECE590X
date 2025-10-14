import d2l

pool = d2l.QuestionPool("test")

question = d2l.MCQuestion("can I put answers on images lets' find out")

for _ in range(4):

    # This technically works but then it can't be transferred to other sections >:(
    question.add_answer('<img src="/content/enforced/7260-sandbox_mjain/imagepools/quantumbeef/ideal.png">', 100)

pool.add_question(question)
pool.package()
pool.dump()