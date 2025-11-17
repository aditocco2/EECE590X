import d2l
import random
import math
from RegularTableHTML.html_table import html_table
from logic_utils.logic_utils import b_format

pool = d2l.QuestionPool("Compute ALU Result")

image_link = "/imagepools/quantumbeef/alu_8b.png"

all_operations = ["F = A", "F = 2 * A", "F = A + B", "F = A - B", "F = B - A", "F = A ^ B", "F = A & B"]
num_operations = 4 # change the image if you change this
op_width = math.ceil(math.log2(num_operations))
opcodes = [b_format(i, op_width) for i in range(num_operations)] # 00, 01, 10, 11

for _ in range(40):
    
    # Make operation table
    operations = random.sample(all_operations, num_operations)
    random.shuffle(operations)
    headers = ["Opcode", "Operation"]
    cols = [opcodes, operations]
    table = html_table(headers, cols)

    # Pick random operation and numbers
    i = random.randrange(num_operations)
    opcode = opcodes[i]
    operation = operations[i]

    A = random.randint(0, 255)
    A_bin = b_format(A, 8)

    B = random.randint(0, 255)
    B_bin = b_format(B, 8)

    # Compute ALU result
    operation = operation.replace(" ", "").replace("F=", "")
    F = eval(operation)
    F_bin = b_format(F, 8)

    # print(f"{operation}, A={A_bin}, B={B_bin} -> F={F_bin}")

    q_text = f"<p> The ALU above has 8-bit inputs <i>A</i> and <i>B</i> and an 8-bit \
        output <i>F</i>. The table below shows its operations: </p> \
        {table} \
        <p> If the opcode is <code>{opcode}</code>, A = <code>{A_bin}</code>, and \
        B = <code>{B_bin}</code>, \
        what is the value of F? <i>Enter your answer in binary.</i></p>"
    
    ans = F_bin
    regex_ans = rf"^[^0-9]*{ans}[^0-9]*$"

    question = d2l.SAQuestion(q_text)
    question.add_image(image_link)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{ans}")

    pool.add_question(question)

pool.package()









