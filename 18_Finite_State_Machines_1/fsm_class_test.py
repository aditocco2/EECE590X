from fsm.fsm_class import FSM

fsm = FSM("fsm_2.txt")

print("=========FSM DATA==========")
print(f"state names: {fsm.state_names}, state bit combos: {fsm.state_bit_combos}")
print(f"input names: {fsm.input_names}, input combos: {fsm.input_combos}")
print(f"outputs: {fsm.output_names}")
print(f"arc data: {fsm.arc_data}")
print(f"state bits: {fsm.state_bit_names}, next_state_bits = {fsm.next_state_bit_names}")

print("rows:")
for row in fsm.rows:
    print(row)

print(f"output columns: {fsm.make_output_columns()}")

html_output = fsm.make_html_truth_table()
with open("tt.html", "w") as f:
    f.write(html_output)
print("wrote truth table to tt.html")

