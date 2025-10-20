import d2l
from fsm.fsm import FSM

pool = d2l.QuestionPool("Analyze Each Arc of State")

text_file = f"FSM_21_E.txt"
image_link = f"/imagepools/quantumbeef/FSM_21_E.png"

fsm = FSM(text_file)

for state in fsm.state_names:
    
    q_text = f"<p>The FSM above was <i>supposed</i> to determine whether two inputs went high \
        at the same time or at different times, but unfortunately, \
        there were a few mistakes in its design.</p> \
        <p>Analyze each of the arcs <i>leaving</i> <b>State {state}</b>, and match each \
        combination of input to its correct description.</p>"

    question = d2l.MQuestion(q_text)
    question.add_image(image_link)
    
    choices = [
        "Valid (one next state specified)",
        "No next state specified",
        "Multiple next states specified"
    ]

    # Add all choices early to not skip one
    for choice in choices:
        question.add_answer(choice=choice)

    # Make each match
    for combo in fsm.input_combos:

        # Make the string on the left
        match = ""
        for input, bit in zip(fsm.input_names, combo):
            match += f"{input} = {bit}, "
        match = match[:-2] # remove comma/space at the end

        # Find out what the deal is with this combo and make the
        # string on the right
        row = fsm.get_row(state, combo)
        if len(row["next_states"]) == 1:
            answer = choices[0]
        elif len(row["next_states"]) == 0:
            answer = choices[1]
        else:
            answer = choices[2]

        question.add_answer(match, answer)

    pool.add_question(question)

pool.package()