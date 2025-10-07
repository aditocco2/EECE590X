from TruthTableHTML.html_tt import html_tt
import json
import re

with open("fsm_2.txt", "r") as f:
    fsm = json.load(f)

# Get states
state_names = []
for node in fsm["fsmNodes"]:
    state_names.append(node["stateName"])
state_names = sorted(state_names)

print(f"state names: {state_names}")

# Get inputs
inputs = []
for arc in fsm["fsmArcs"]:
    text = arc["outputText"]
    # replace everything but alphanumeric and underscore with space
    text = re.sub("[^0-9a-zA-Z_]+", " " , text)
    arc_inputs = text.split(" ")
    # Put non-empty, non-duplicate strings
    inputs = inputs + [i for i in arc_inputs if i and i not in inputs]

print(f"inputs: {inputs}")

# Get Moore outputs
outputs = []
for node in fsm["fsmNodes"]:
    text = node["outputText"]
    # replace everything but alphanumeric and underscore with space
    text = re.sub("[^0-9a-zA-Z_]+", " " , text)
    node_outputs = text.split(" ")
    # Put non-empty, non-duplicate strings that don't start with a number
    outputs = outputs + [o for o in node_outputs if o and o not in outputs and not o[0].isdigit()]

print(f"outputs: {outputs}")


# Now make the truth table...

num_state_bits = len(state_names[0])
num_input_bits = len(inputs)

num_rows = 2 ** (num_input_bits + num_state_bits)
print(f"rows: {num_rows}")

# Find all possible combinations of state bits, even if unused
# For example:
# if state_names is ["00", "01", "10"]
# this makes state_bit_combos ["00", "01", "10", "11"]

state_bit_combos = [f"{i:0{num_state_bits}b}" for i in range(2 ** num_state_bits)]
print(f"all possible state bit combos: {state_bit_combos}")

# Find all possible combinations of the input
input_combos = [f"{i:0{num_input_bits}b}" for i in range(2 ** num_input_bits)]
print(f"all possible input combos: {input_combos}")

for state in state_bit_combos:
    # Since arcs anchor to node ID and not state name, we have to use the arc's
    # start node ID to index into the list of states
    leaving_arcs = [arc for arc in fsm["fsmArcs"] 
                    if fsm["fsmNodes"][arc["startNode"]]["stateName"] == state]
    
    print(f"state: {state}, arcs {leaving_arcs}")