import d2l

pool = d2l.QuestionPool("Add Sub Inc Dec") # don't know a better name

variants = ["add", "sub", "inc", "dec"]
for variant in variants:

    if variant == "add":  
        image = "two_bit_adder_skeleton.png"
        placeholder = "<b>2-bit adder</b>"
        answers = ["B[1]", "C[0]", "A[0]", "B[0]", "Constant 0"]
        distractors = ["Constant 1", "C[1]", "B[1]'", "B[0]'"]

    elif variant == "sub":  
        image = "two_bit_adder_skeleton.png"
        placeholder = "<b>2-bit subtractor</b> using two's complement"
        answers = ["B[1]'", "C[0]", "A[0]", "B[0]'", "Constant 1"]
        distractors = ["Constant 0", "C[1]", "B[1]", "B[0]"]

    elif variant == "inc":
        image = "two_bit_incrementer_skeleton.png"
        placeholder = "<b>2-bit incrementer</b>, which adds 1 to a number"
        answers = ["Constant 0", "C[0]", "A[0]", "Constant 1"]
        distractors = ["C[1]", "S[1]", "S[0]"]

    elif variant == "dec":
        image = "two_bit_incrementer_skeleton.png"
        placeholder = "<b>2-bit decrementer</b>, which subtracts 1 from a number using two's complement"
        answers = ["Constant 1", "C[0]", "A[0]", "Constant 1"]
        distractors = ["Constant 0", "C[1]", "A[1]'", "A[0]'"]

    q_text = f"<p> Suppose you have built a 1-bit adder block using combinational logic. \
    You want to chain these together to create a {placeholder}. </p> \
    <p> A diagram is shown above with placeholders for the inputs to the adders. \
    Determine which signals should be connected to each input, and match them below. </p>"

    matches = [f"Input {i+1}" for i in range(len(answers))]
    image_link = f"/imagepools/quantumbeef/{image}"

    question = d2l.MQuestion(q_text, shuffle=True)
    question.add_image(image_link)
    
    # Add all answers first to avoid cheese (1st answer being on top)
    for c in answers + distractors:
        question.add_answer(choice = c)
    
    # Then add matches with correct ones
    for match, choice in zip(matches, answers):
        question.add_answer(match, choice)

    pool.add_question(question)

pool.package()

    


