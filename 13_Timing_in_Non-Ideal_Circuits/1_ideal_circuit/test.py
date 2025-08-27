import wave_utils as wu

a_bin, a_wave = wu.make_random_signal(20)
b_bin, b_wave = wu.make_random_signal(20)

print(f"a:\nbinary:   {a_bin:0{20}b}\nwavedrom: {a_wave}")
print(f"b:\nbinary:   {b_bin:0{20}b}\nwavedrom: {b_wave}")

# a and not b
answer = a_bin & ~b_bin
answer = f"{a_bin:0{20}b}"
print(f"answer:   {answer}")

# q = wu.make_question_text("Question 1", ["a", "b"], [w1, w2], ["F"])
# print(q)