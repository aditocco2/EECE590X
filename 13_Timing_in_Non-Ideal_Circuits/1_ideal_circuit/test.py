from wave_utils import *

a = make_random_signal(20)
b = make_random_signal(20)

f = wavedrom_gate("xor", a, b, 0)

print(f"a: {a}\nb: {b}\nf: {f}")

q = make_question_link("Question 1", ["a", "b"], [a, b], ["F"])
print(q)