import d2l
import random
import math
from html_utils.html_utils import html_table

pool = d2l.QuestionPool("Determine ALU Opcode Width")

all_operations = ["F = 0", "F = A", "F = B", "F = A + 1", "F = A - 1", "F = 2A", "F = A + B", "F = A * B", "F = A - B", "F = A ^ B", "F = A & B"]

for i in range(40):
    
    # Get a bunch of random operations and find the necessary bit width
    num_operations = random.randint(3, 10)
    operations = random.sample(all_operations, num_operations)
    random.shuffle(all_operations)

    ans = math.ceil(math.log2(len(operations)))
    
    # Make ALU operation table
    headers = ["Opcode", "Operation"]
    col1 = ["?" for _ in operations]
    col2 = operations
    cols = [col1, col2]
    table = html_table(headers, cols)

    q_text = f"<p>Suppose you are designing an arithmetic logic unit with a specific set of \
        functionalities. You have started filling out the operation table below: <p> \
        {table} \
        <p> What is the minimum bit width the opcode would need to be to accomodate all of these operations?"
    
    regex_ans = rf"^[^0-9]*{ans}[^0-9]*$"

    question = d2l.SAQuestion(q_text)
    question.add_answer(regex_ans, is_regex=True)
    question.add_feedback(f"{ans} bits")

    pool.add_question(question)

pool.package()