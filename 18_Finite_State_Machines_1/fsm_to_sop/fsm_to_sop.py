import d2l
import random
from fsm.fsm_class import FSM

pool = d2l.QuestionPool("FSM to SOP matching")

variants = "IJKL"

# Make all the sums of products
all_sops_dict = {}
all_sops_list = []
for q_letter in variants:
    fsm_name = f"FSM_18_{q_letter}"
    fsm_filename = fsm_name + ".txt"
    fsm = FSM(fsm_filename, fsm_name)
    
    expressions = fsm.find_output_expressions()

    all_sops_dict[q_letter] = expressions
    
    all_sops_list += [expressions[output] for output in expressions]

    # To make sure they're all properly specified
    # print(fsm_name)
    # for row in fsm.rows:
    #     print(row)  

# Remove duplicates
temp = []
for i in all_sops_list:
    if i not in temp:
        temp.append(i)
all_sops_list = temp

# Make questions
for q_letter in variants:

    q_text = ("For the FSM model above, match the next state bits and outputs " +
              "to their Boolean expressions.")
    image_link = f"/imagepools/quantumbeef/FSM_18_{q_letter}.png"

    question = d2l.MQuestion(q_text, shuffle=True)
    question.add_image(image_link)

    correct_sops_dict = all_sops_dict[q_letter]

    # Sample some wrong ones as distractors
    correct_sops_list = [correct_sops_dict[output] for output in correct_sops_dict]
    wrong_sops_list = [sop for sop in all_sops_list if sop not in correct_sops_list]
    wrong_sops = random.sample(wrong_sops_list, 3)

    # Add correct choices
    for output in correct_sops_dict:
        sop = correct_sops_dict[output]
        question.add_answer(output, sop)

    # Add distractors
    for sop in wrong_sops:
        question.add_answer(choice=sop)

    pool.add_question(question)

pool.package()
    
