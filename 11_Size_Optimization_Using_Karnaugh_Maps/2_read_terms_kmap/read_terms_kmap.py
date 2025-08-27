import d2l
import random
from schemdraw_kmap import draw_kmap

pool = d2l.QuestionPool("Determine Kmap Terms", "pool.csv")

groups = {
        ("1..1",".000") : ["ad","b'c'd'"],
        ("11..",".0.0") : ["ab","b'd'"],
        ("111.",".01.") : ["abc","b'c"],
        ("001.","0..0") : ["a'b'c","a'd'"],
        ('101.','00.1','.111') : ["ab'c","a'b'd","bcd"],

        }

count = 0

for key in groups:
    draw_kmap(key,f'kmap_{count}')

    question_text = f"<p>Determine the algebraic expression for the \
            terms circled in the Karnaugh Map shown above.</p>"


    question = d2l.SAQuestion(question_text)

    ans = "|".join(groups[key])
    regex_ans = "^"
    feedback = "+".join(groups[key])

    for i in range(len(groups[key])-1):
        regex_ans += f"\\s*({ans})(?!.*\\{i+1}[^'a-z])\\s*\\+"
    regex_ans += f"\\s*({ans})\\s*$"
    question.add_image(f"/imagepools/alivebeef/kmap_{count}.png")
    question.add_answer(f"{regex_ans}", is_regex = True)
    question.add_feedback(feedback)
    pool.add_question(question)
    count = count + 1

pool.dump()
pool.package()


