import d2l
import random
from RegularTableHTML.html_table import html_table

pool = d2l.QuestionPool("Match Opcodes with Operations")

# For distractors
all_operations = ["F = 0", "F = A", "F = B", "F = A + 1", "F = A - 1", "F = 2A", "F = A + B", "F = A - B"]

correct_operations = {
    "A" : ["F = A", "F = B", "F = A + B", "F = 2A"],
    "B" : ["F = 0", "F = B", "F = A + B", "F = A - B"],
    "C" : ["F = B", "F = A + B", "F = A - B", "F = 0"],
    "D" : ["F = A + B", "F = A - B", "F = A + 1", "F = A - 1"]
}
opcodes = ["00", "01", "10", "11"]

letters = ["A", "B", "C", "D"]

for letter in letters:
    image_link = f"/imagepools/quantumbeef/ALU_27_{letter}.png"

    q_text = "<p> For the ALU pictured above, match each opcode to its \
         corresponding operation. </p>"
    
    question = d2l.MQuestion(q_text, shuffle=True)
    question.add_image(image_link)

    # Add all first
    for operation in all_operations:
        question.add_answer(choice=operation)

    # Make the correct matches
    for opcode, operation in zip(opcodes, correct_operations[letter]):
        question.add_answer("Opcode " + opcode, operation)

    pool.add_question(question)

pool.package()
    
