import d2l
import random
import re
import schemdraw
import schemdraw.elements as elm
from schemdraw.parsing import logicparse as lp
from wavedrom_setup import generate_wavedrom as gen

pool = d2l.QuestionPool("Make WaveDrom from Circuit", "pool.csv")

# Labels will not work on server's version of schemdraw
d = lp('(a and b) or (not a and not b)', outlabel='F')
d.save("ideal.svg")

'''
d1 = lp('(a and b) or (not a and not b)', outlabel='F')
d1.add(elm.Label('2 ns', color='red').at((-1.05, -1.75)))
d1.add(elm.Label('2 ns', color='red').at((-3.05, -1)))
d1.add(elm.Label('2 ns', color='red').at((-3.05, -2.5)))
d1.add(elm.Label('1 ns', color='red').at((-4.55, -2.5)))
d1.add(elm.Label('1 ns', color='red').at((-4.55, -1)))
d1.save("non_ideal.png")
'''

for i in range(1):
    wavedrom_call = gen('EECE 251 HW 13 Question 1',['a','b'],["ab","a'","b'","a'b'","F"])
    question_text = f"<p>The circuit above is <i>ideal</i> and ignores \
            gate delays. Click on the wavedrom text below to open the \
            problem in Watson Wiki. You may also copy and paste the text \
            into the wavedrom editor website.</p>"+\
            f"<p>{wavedrom_call}</p>"+\
            f"<p><b>When you are finished recreating the waveforms, please \
            copy and paste the wave for 'F' as your answer in the box below.</b></p>"
    

    question = d2l.SAQuestion(question_text)

    input_array = re.findall(r'wave:\s*"([hl\.]*)"',wavedrom_call)
    sig_a = [i for i in input_array[0]]
    sig_b = [i for i in input_array[1]]
    for i in range(len(sig_a)):
        if sig_a[i] == '.':
            sig_a[i] = sig_a[i-1]
    for i in range(len(sig_b)):
        if sig_b[i] == '.':
            sig_b[i] = sig_b[i-1]
    for i in range(len(sig_a)):
        if sig_b[i] == '.':
            sig_b[i] = sig_b[i-1]
    print("".join(sig_a))
    print("".join(sig_b))

    sig_f = ['h' if a==b else 'l' for a,b in zip(sig_a,sig_b)]
    print("".join(sig_f))
    for i in reversed(range(len(sig_f))):
        if sig_f[i] == sig_f[i-1] and i != 0:
            sig_f[i] = '.'
    
    print("".join(sig_f))
    # choke
    # why tf is the above here

    regex_ans = f"(wave:)*\s*'*{sig_f}'*"
    feedback = "Answer should have 20 characters and look like 'h...l.h..l..........'"

    for i in range(1): # range(len(groups[key])-1):
        regex_ans += f"\\s*()(?!.*\\{i+1}[^'a-z])\\s*\\+"
    regex_ans += f"\\s*()\\s*$"
    question.add_image(f"/imagepools/alivebeef/ideal.png")
    question.add_answer(f"{regex_ans}", is_regex = True)
    question.add_feedback(feedback)
    pool.add_question(question)

#pool.dump()
print(wavedrom_call)
pool.package()


