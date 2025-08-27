import d2l
import math

pool = d2l.QuestionPool("How many bits to encode a value SA", "pool.csv")

number_questions = 257

for i in range(2, number_questions):
    question = d2l.SAQuestion( f"How many bits are required to encode {i}" \
            " values?") # make dict for values: things, values, items
    answer = math.ceil(math.log2(i)) 
    question.add_answer(f"^\\s*{str(answer)}\\s*$", is_regex = True)
    question.add_feedback(str(answer))
    pool.add_question(question)

pool.dump()
pool.package()
