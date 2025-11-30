import d2l
import random
import math
import wave_utils.wave_utils as wu
import image_utils.image_utils as img
from html_utils.html_utils import html_table
from logic_utils.logic_utils import b_format

pool = d2l.QuestionPool("Choose ALU Table from Timing Diagram")

all_operations = ["F = A", "F = 2 * A", "F = A + B", "F = A - B", "F = B - A", "F = A ^ B", "F = A & B"]
num_operations = 4
op_width = math.ceil(math.log2(num_operations))
opcodes = [b_format(i, op_width) for i in range(num_operations)] # 00, 01, 10, 11

# 6 variants
for letter in "ABCDEF":
    
    image_name = f"diagram_28_{letter}.png"
    image_name_svg = f"diagram_28_{letter}.svg"
    image_link = f"/imagepools/quantumbeef/{image_name}"

    operations = random.sample(all_operations, num_operations)
    random.shuffle(operations)

    # Make the WaveDrom image
    A = wu.make_random_buses(20, 4)
    B = wu.make_random_buses(20, 4)
    op = wu.make_random_timing_of_buses(opcodes, 20)
    F = wu.wavedrom_alu(A, B, op, opcodes, operations)
    wu.make_wavedrom_image_with_buses("q27_4", ["A", "B", "opcode", "F"],
                                  [A, B, op, F], image_name_svg)
    img.svg2png(image_name_svg, image_name)

    q_text = f"<p> An ALU has 4-bit inputs A and B and a 2-bit opcode. \
        Based on the timing diagram above, what is the correct operation table \
        for this ALU? </p>"
    question = d2l.MCQuestion(q_text)
    question.add_image(image_link)
    
    headers = ["Opcode", "Operation"]
    
    # Make right answer
    cols = [opcodes, operations]
    table = html_table(headers, cols)
    question.add_answer(table, 100)

    # Make 3 wrong answers
    for _ in range(0, 3):
        wrong_operations = operations.copy()
        random.shuffle(wrong_operations)

        cols = [opcodes, wrong_operations]
        table = html_table(headers, cols)
        question.add_answer(table, 0)

    pool.add_question(question)

pool.package()









