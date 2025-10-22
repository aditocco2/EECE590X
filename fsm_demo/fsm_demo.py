from fsm.fsm import FSM

# Uncomment an FSM to load from file:

# Mealy pulser
# fsm = FSM("fsms/FSM_1.txt")
# Moore pulser
# fsm = FSM("fsms/FSM_2.txt")
# Detects if two inputs went high at the same time or different times
fsm = FSM("fsms/FSM_3.txt") 
# Improperly specified version of 3
# fsm = FSM("fsms/FSM_4_improper.txt")
# Super simple one with no inputs
# fsm = FSM("fsms/FSM_5_no_input.txt")

print(f"{"="*30}{fsm.name} DATA{"="*30}")

# When you load the FSM, all the data gets extracted from the JSON file
# and organized into every possible combo of state and input:
print(f"States: {fsm.state_names}")
print(f"Moore outputs: {fsm.moore_names}")
print(f"Mealy outputs: {fsm.mealy_names}")
print("All combos:")
for row in fsm.rows:
    print(row)

# Making sure it's properly specified:
fsm.verify()

# This can be made into the state table:
html_output = fsm.make_html_truth_table()
with open("state_table.html", "w") as f:
    f.write(html_output)
print("Wrote HTML TT to state_table.html")

# Or the sum of products for each state bit / output (with or without reset):
expressions = fsm.find_output_expressions(include_reset=False)
print(f"Output expressions: {expressions}")
if fsm.has_reset:
    expressions = fsm.find_output_expressions(include_reset=True)
    print(f"Output expressions with reset: {expressions}")

# Lastly, we can follow the FSM with a specified input pattern

# (a bunch of setup, this is just to accomodate the number of inputs
# for whatever FSM is selected)
if fsm.num_inputs == 0:
    sequence = 7 # just a number of clock cycles
elif fsm.num_inputs == 1:
    sequence = "00111010"
else:
    sequence = ["00", "10", "10", "11", "00", "11", "11", "00"]

if fsm.num_state_bits == 1:
    start_state = "0"
elif fsm.num_state_bits == 2:
    start_state = "00"
elif fsm.num_state_bits == 3:
    start_state = "000"
    
print(f"Following {fsm.name} from state {start_state}:")
# Follow the FSM
end_state, state_sequence, output_sequence = fsm.follow(sequence, start_state)
print(f"State sequence: {state_sequence}")
print(f"Output sequence: {output_sequence}")
print(f"Ending state: {end_state}")