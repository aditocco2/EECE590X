import d2l
import random
from logic_utils.logic_utils import b_format
from RegularTableHTML.html_table import html_table

pool = d2l.QuestionPool("Match MFR Operation w/ ALU Operation")

image_link = "/imagepools/quantumbeef/MFR_28_1.png"

# MFR operation on left, ALU operation on right
operation_bank = {
    "Q <- Q" : "F = R", # hold
    "Q <- A" : "F = L", # load
    "Q <- 0" : "F = 0", # reset
    "Q <- Q + A" : "F = L + R", # add
    "Q <- Q - A" : "F = R - L", # sub
    "Q <- 2Q" : "F = 2R", # double
    "Q <- Q + 1" : "F = R + 1", # inc
    "Q <- Q - 1" : "F = R - 1", # dec
}

distractors = ["F = L - R", "F = L + 1", "F = L - 1", "F = 2L"]

num_operations = 5
opcode_bits = num_operations - 1


for _ in range(40):

    # Make opcode 0 always hold
    opcodes = [b_format(0, opcode_bits)]
    mfr_operations = ["Q <- Q"]

    # Add 0001, 0010, etc. to opcode list
    for i in range(0, opcode_bits):
        opcodes.append(b_format(1 << i, opcode_bits))
        
    # Randomly pick the rest of the MFR operations
    ops_minus_hold = list(operation_bank.keys())
    ops_minus_hold.remove("Q <- Q")
    mfr_operations += random.sample(ops_minus_hold, num_operations - 1)

    alu_operations = [operation_bank[m] for m in mfr_operations]
    
    all_choices = alu_operations + random.sample(distractors, 2)

    headers = ["Opcode", "MFR Operation"]
    cols = [opcodes, mfr_operations]

    table = html_table(headers, cols)

    q_text = f"<p> The multi-function register shown above has the following \
        operation table: </p> \
        {table} \
        <p> Match the MFR opcodes with their corresponding <b>ALU operations</b> below. </p>"
    
    question = d2l.MQuestion(q_text, shuffle=True)
    question.add_image(image_link)

    # Add all first
    for choice in all_choices:
        question.add_answer(choice=choice)

    # Make the correct matches
    for opcode, operation in zip(opcodes, alu_operations):
        question.add_answer("Opcode " + opcode, operation)

    pool.add_question(question)

pool.package()

    


