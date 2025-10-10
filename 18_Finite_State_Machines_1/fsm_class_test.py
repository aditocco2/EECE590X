import fsm_data

fsm = fsm_data.FSMData("fsm_2.txt")

print(f"state names: {fsm.state_names}, state bit combos: {fsm.state_bit_combos}")
print(f"input names: {fsm.input_names}, input combos: {fsm.input_combos}")
print(f"outputs: {fsm.output_names}")
print(f"state data: {fsm.state_data}")
print(f"state bits: {fsm.state_bit_names}, next_state_bits = {fsm.next_state_bit_names}")

output_columns = fsm.make_output_columns()
print(f"output columns: {output_columns}")

rows = fsm.evaluate_all_combos()
print(f"rows: {rows}")
