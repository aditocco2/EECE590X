import d2l
import random
from RegularTableHTML.html_table import html_table

pool = d2l.QuestionPool("Choose Correct Operation Table")

# For distractors
all_operations = ["F = 0", "F = A", "F = B", "F = A + 1", "F = A - 1", "F = 2A", "F = A + B", "F = A * B", "F = A - B", "F = A ^ B", "F = A & B"]

headers = ["Opcode", "Operation"]
op_cols = {
    "A" : ["F = A", "F = B", "F = A + B", "F = 2A"],
    "B" : ["F = 0", "F = B", "F = A + B", "F = A - B"],
    "C" : ["F = B", "F = A + B", "F = A - B", "F = 0"],
    "D" : ["F = A + B", "F = A - B", "F = A + 1", "F = A - 1"]
}
opcodes = ["00", "01", "10", "11"]

letters = ["A", "B", "C", "D"]

for letter in letters:
    image_link = f"/imagepools/quantumbeef/ALU_27_{letter}.png"

    q_text = "<p> What is the correct operation table for the \
        arithmetic logic unit pictured above? </p>"
    
    right_col = op_cols[letter]
    right = html_table(headers, [opcodes, right_col])

    # shuffle columns of correct table
    d_col_1 = op_cols[letter]
    random.shuffle(d_col_1)
    wrong_1 = html_table(headers, [opcodes, d_col_1])

    # get table from a different ALU
    temp = letters.copy()
    temp.remove(letter)
    d_letter = random.choice(temp)
    d_col_2 = op_cols[d_letter]
    wrong_2 = html_table(headers, [opcodes, d_col_2])

    # Get random operations
    d_col_3 = random.sample(all_operations, 4)
    while d_col_3 == right_col: # really rare but just to be sure
        d_col_3 = random.sample(all_operations, 4)
    wrong_3 = html_table(headers, [opcodes, d_col_3])

    question = d2l.MCQuestion(q_text)
    question.add_image(image_link)
    question.add_answer(right, 100)
    question.add_answer(wrong_1, 0)
    question.add_answer(wrong_2, 0)
    question.add_answer(wrong_3, 0)

    pool.add_question(question)

pool.package()
    
