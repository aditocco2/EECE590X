from fsm.fsm import FSM

# Pick an FSM to load from file:
fsm = FSM("FSM_1.txt") # Mealy pulser
# (Add more)

print(f"{"="*20}{fsm.name} DATA{"="*20}")

# When you load the FSM, all the data gets extracted from the JSON file
# and organized into every possible combo of state and input:
print(f"States: {fsm.state_names}")
print(f"Moore outputs: {fsm.moore_names}")
print(f"Mealy outputs: {fsm.mealy_names}")
print("All combos:")
for row in fsm.rows:
    print(row)

# This can be made into the state table:
html_output = fsm.make_html_truth_table()
with open("state_table.html", "w") as f:
    f.write(html_output)
print("Wrote HTML TT to state_table.html")

# Or the sum of products for each state bit / output:
sops_dict = fsm.find_output_expressions()
print(f"Output expressions: {sops_dict}")







