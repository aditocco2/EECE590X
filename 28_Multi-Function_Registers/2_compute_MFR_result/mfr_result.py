import d2l
import random
from logic_utils.logic_utils import b_format
from html_utils.html_utils import html_table

pool = d2l.QuestionPool("Find MFR Result")

image_link = "/imagepools/quantumbeef/MFR_28_1.png"

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

num_operations = 5 # change picture if changing this
opcode_bits = num_operations - 1

for _ in range(40):

    # MAKE TABLE

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

    headers = ["Opcode", "MFR Operation"]
    cols = [opcodes, operations]

    table = html_table(headers, cols)

    # COMPUTE RESULT

    # pick random numbers for Q and A
    Q = random.randint(0, 255)
    Q_bin = b_format(Q, 8)
    A = random.randint(0, 255)
    A_bin = b_format(A, 8)

    indices = random.choices(range(len(opcodes)), k=3) # change wording of question if changing k
    opcode_sequence = [opcodes[i] for i in indices]
    operation_sequence = [operations[i] for i in indices]

    # Make them evaluable
    operation_sequence = [s.replace("Q <- ", "") for s in operation_sequence]

    for operation in operation_sequence:
        Q = eval(operation)

    ans = b_format(Q, 8)

    # NOW FORM QUESTION

    q_text = f"<p> The multi-function register pictured above has the following \
        operation table: </p> \
        {table} \
        <p> The value of Q is initially <code>{Q_bin}</code>. The value of A is <code>{A_bin}</code>, \
        and it stays constant. The MFR receives opcodes of <code>{opcode_sequence[0]}</code>, \
        <code>{opcode_sequence[1]}</code>, and <code>{opcode_sequence[2]}</code> over the next \
        three clock cycles.</p> \
        <p> What is the resulting value of Q? <i>Enter your answer in binary.</i></p>"
    
    regex_ans = rf"^[^0-9]*{ans}[^0-9]*$"

    question = d2l.SAQuestion(q_text)
    question.add_image(image_link)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(ans)

    pool.add_question(question)

pool.package()
