import d2l
from fsm.fsm import FSM

pool = d2l.QuestionPool("Analyze Each State of FSM")

variants = "ABCD"

# What the FSMs were supposed to do``
descriptions = {
    "A": "count upwards in place if the input is high and stay in the same state otherwise",
    "B": "detect when the input goes from 0 to 1",
    "C": "toggle the output when the input changes from 0 to 1",
    "D": "detect four cycles of high input in a row"
}

for letter in variants:
    
    text_file = f"FSM_21_{letter}.txt"
    image_link = f"/imagepools/quantumbeef/FSM_21_{letter}.png"
    q_text = f"<p>The FSM above was <i>supposed</i> to {descriptions[letter]}, but unfortunately, \
            there were a few mistakes in its design. Analyze each state of this FSM and match it \
                with the correct description.</p>"

    fsm = FSM(text_file)

    question = d2l.MQuestion(q_text)
    question.add_image(image_link)

    choices = [
        "This state is properly specified",
        "The transitions are incomplete",
        "The transitions are non-exclusive",
        "The transitions are both incomplete and non-exclusive"
    ]

    # Add the choices early so that none get missed
    for choice in choices:
        question.add_answer(choice=choice)

    for state in fsm.state_names:

        # Determine if each state is incomplete, nonexclusive, or both
        incomplete = False
        nonexclusive = False
        rows = fsm.get_rows_from_state(state)
        for row in rows:
            if len(row["next_states"]) == 0:
                incomplete = True
            elif len(row["next_states"]) > 1:
                nonexclusive = True

        if not incomplete and not nonexclusive:
            answer = choices[0]
        elif incomplete and not nonexclusive:
            answer = choices[1]
        elif not incomplete and nonexclusive:
            answer = choices[2]
        elif incomplete and nonexclusive:
            answer = choices[3]
        else:
            raise Exception("how")

        question.add_answer(f"State {state}", answer)
    
    pool.add_question(question)
    
pool.package()