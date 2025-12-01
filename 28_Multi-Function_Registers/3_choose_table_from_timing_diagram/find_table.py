import d2l
import random
import math
import wave_utils.wave_utils as wu
import image_utils.image_utils as img
from html_utils.html_utils import *
from logic_utils.logic_utils import b_format

pool = d2l.QuestionPool("Choose MFR Table from Timing Diagram")

operation_bank = [
    "Q <- Q", # hold
    "Q <- A", # load
    "Q <- 0", # reset
    "Q <- Q + A", # add
    "Q <- Q - A", # sub
    "Q <- 2 * Q", # double
    "Q <- Q + 1", # inc
    "Q <- Q - 1", # dec
    "Q <- Q ^ A", # xor
    "Q <- Q & A" # and
]
num_operations = 4
opcode_bits = num_operations - 1

# 6 variants
for letter in "ABCDEF":
    
    image_name = f"diagram_28_{letter}.png"
    image_name_svg = f"diagram_28_{letter}.svg"
    image_link = f"/imagepools/quantumbeef/{image_name}"

    # Make opcode 0 always hold
    opcodes = [b_format(0, opcode_bits)]
    operations = ["Q <- Q"]

    # Add 0001, 0010, etc. to opcode list
    for i in range(0, opcode_bits):
        opcodes.append(b_format(1 << i, opcode_bits))
        
    # Randomly pick the rest of the MFR operations
    ops_minus_hold = operation_bank.copy()
    ops_minus_hold.remove("Q <- Q")
    operations += random.sample(ops_minus_hold, num_operations - 1)

    # Make the WaveDrom image
    Q_start = b_format(random.randint(0, 15), 4)
    A = wu.make_random_buses(20, 4)
    op = wu.make_random_timing_of_buses(opcodes, 20)
    clk = wu.make_clock(20, 4, 2)
    Q = wu.wavedrom_mfr(clk, Q_start, A, op, opcodes, operations)
    wu.make_wavedrom_image_with_buses("q28_3", ["clk", "A", "opcode", "Q"],
                                  [clk, A, op, Q], image_name_svg)
    img.svg2png(image_name_svg, image_name, dpi=200)

    # print(f"{Q_start}\n{clk}\n{A}\n{op}\n{Q}")

    q_text = f"<p> A multi-function register has a 4-bit data input {italic("A")}, \
        a 4-bit data output {italic("Q")}, and a {opcode_bits}-bit opcode. \
        Based on the timing diagram above, what is the correct table for this MFR? </p>"
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

        # make sure shuffle doesn't do nothing
        while wrong_operations == operations:
            random.shuffle(wrong_operations)

        cols = [opcodes, wrong_operations]
        table = html_table(headers, cols)
        question.add_answer(table, 0)

    pool.add_question(question)

pool.package()