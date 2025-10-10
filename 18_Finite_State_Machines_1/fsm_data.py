from TruthTableHTML.html_tt import html_tt
from logic_eval import logic_eval
import itertools
import json
import re

class FSMData():

    def __init__(self, filename, state_notation = "Q"):
        with open(filename, "r") as f:
            self.fsm_json = json.load(f)
        self.get_inputs_from_json()
        self.get_outputs_from_json()
        self.get_states_from_json(state_notation)
        self.organize_state_data()
    
    def organize_state_data(self):

        # Makes a list of states with all their arcs and outputs

        self.state_data = []

        for current_state in self.state_names:

            current_state_data = {"state": current_state, "outputs": {}, "arcs": []}

            # Find the output text corresponding to the current state
            for node in self.fsm_json["fsmNodes"]:
                if node["stateName"] == current_state:
                    text = node["outputText"]
            # replace everything but alphanumeric and underscore with space
            text = re.sub("[^0-9a-zA-Z_]+", " " , text)
            output_words = text.split(" ") #["F", "1", "G", "0"]

            for output in self.output_names:
                # If an output exists under the state name, copy it to the outputs dict
                if output in output_words:
                    output_value = output_words[output_words.index(output) + 1]
                    current_state_data["outputs"][output] = str(output_value)
                # Otherwise assume it's 0
                else:
                    current_state_data["outputs"][output] = "0"

            # Since arcs anchor to node ID and not state name, we have to use the arc's
            # start node ID to index into the list of states
            # They are also stored in two separate lists: fsmArcs and fsmSelfArcs
            
            for arc in self.fsm_json["fsmArcs"]:
                state_arc_leaves = self.fsm_json["fsmNodes"][arc["startNode"]]["stateName"]
                state_arc_goes_to = self.fsm_json["fsmNodes"][arc["endNode"]]["stateName"]
                if state_arc_leaves == current_state:
                    arc_dict = {"expression": arc["outputText"],
                                "next_state": state_arc_goes_to}
                    current_state_data["arcs"].append(arc_dict)

            for arc in self.fsm_json["fsmSelfArcs"]:
                state_arc_is_on = self.fsm_json["fsmNodes"][arc["node"]]["stateName"]
                if state_arc_is_on == current_state:
                    arc_dict = {"expression": arc["outputText"],
                                "next_state": state_arc_is_on}
                    current_state_data["arcs"].append(arc_dict)
                    
            self.state_data.append(current_state_data)

    def get_states_from_json(self, notation = "Q"):
        self.state_names = []
        for node in self.fsm_json["fsmNodes"]:
            self.state_names.append(node["stateName"])
        self.state_names = sorted(self.state_names)

        num_state_bits = len(self.state_names[0])
        self.state_bit_combos = [f"{i:0{num_state_bits}b}" for i in range(2 ** num_state_bits)]

        # Make state bit names like Q1, Q0, Q1+, Q0+
        self.state_bit_names = [notation + str(i) for i in range(num_state_bits)]
        self.state_bit_names.reverse()
        self.next_state_bit_names = [i + "+" for i in self.state_bit_names]
    
    def get_inputs_from_json(self):
        if self.fsm_json["inputs"]:
            self.input_names = self.fsm_json["inputs"].replace(" ", "").split(",")
        else:
            inputs = []
            for arc in self.fsm_json["fsmArcs"] + self.fsm_json["fsmSelfArcs"]:
                text = arc["outputText"]
                # replace everything but alphanumeric and underscore with space
                text = re.sub("[^0-9a-zA-Z_]+", " " , text)
                arc_inputs = text.split(" ")
                # Put non-empty, non-duplicate strings
                inputs = inputs + [i for i in arc_inputs if i and i not in inputs]
            # Remove strings that are made up of other strings, like "ab"
            for i in inputs:
                for j in inputs:
                    if i + j in inputs:
                        inputs.remove(i + j)
            self.input_names = inputs
            
        num_input_bits = len(self.input_names)
        self.input_combos = [f"{i:0{num_input_bits}b}" for i in range(2 ** num_input_bits)]

    def get_outputs_from_json(self):
    # Get Moore outputs
        outputs = []
        for node in self.fsm_json["fsmNodes"]:
            text = node["outputText"]
            # replace everything but alphanumeric and underscore with space
            text = re.sub("[^0-9a-zA-Z_]+", " " , text)
            node_outputs = text.split(" ")
            # Put non-empty, non-duplicate strings that don't start with a number
            outputs = outputs + [o for o in node_outputs if o and o not in outputs and not o[0].isdigit()]
        self.output_names = outputs

    def make_output_columns(self):

        output_columns = {}

        # Initialize output columns
        for output in self.next_state_bit_names + self.output_names:
            output_columns[output] = ""

        # make all possible combinations of state with input
        # (sorta like TT rows but without the outputs)
        all_combos = itertools.product(self.state_bit_combos, self.input_combos)

        num_state_bits = len(self.state_bit_combos[0])

        # Then drill the logic
        for combo in all_combos:
            state_combo = combo[0]
            input_combo = combo[1]

            # Get the dictionary with the appropriate state
            state_datum = [d for d in self.state_data if d["state"] == state_combo]

            # If the state combo is used, figure out the appropriate next state
            if state_datum:
                state_datum = state_datum[0]
                current_state = state_datum["state"]

                # Process the arc to get the next state
                arcs = state_datum["arcs"]
                for arc in arcs:
                    expression = arc["expression"]
                    # If the expression on the arc evaluates to true (or it's empty)
                    # Copy the arc's next state into the truth table
                    if not expression or logic_eval(self.input_names, input_combo, expression):
                        for i, column in zip(range(num_state_bits), self.next_state_bit_names):
                            # 7 LEVELS OF INDENTATION I AM THE BEST PROGRAMMER TO WALK THIS EARTH RAAAAAAAHHHH
                            output_columns[column] += arc["next_state"][i]
                    # Otherwise copy the current state into the truth tablex
                    # else:
                    #     for i, column in zip(range(num_state_bits), self.next_state_bit_names):
                    #         output_columns[column] += current_state[i]
                
                # Process the current state to get the Moore output
                for output in self.output_names:
                    if state_datum["outputs"][output] == "1":
                        output_columns[output] += "1"
                    else:
                        output_columns[output] += "0"
            
            # If the state combo is unused:
            else:
                # Don't care next state / output
                for column in self.next_state_bit_names + self.output_names:
                    output_columns[column] += "x"
                
        self.output_columns = output_columns        
        return output_columns
    

    def evaluate_all_combos(self):

        rows = []

        # Initialize output columns

        # make all possible combinations of state with input
        # (sorta like TT rows but without the outputs)
        all_combos = itertools.product(self.state_bit_combos, self.input_combos)

        # Then drill the logic
        for combo in all_combos:

            state_combo = combo[0]
            input_combo = combo[1]

            row = {}
            row["state"] = state_combo
            for i in range(len(combo[1])):
                row[self.input_names[i]] = input_combo[i]
            # A list, so we can check for improperly specified FSMs
            row["next_states"] = []

            # Get the dictionary with the appropriate state
            state_datum = [d for d in self.state_data if d["state"] == state_combo]

            # If the state combo is used, figure out the appropriate next state
            if state_datum:
                state_datum = state_datum[0]

                # Process the arc to get the next state
                arcs = state_datum["arcs"]
                for arc in arcs:
                    expression = arc["expression"]
                    # If the expression on the arc evaluates to true (or it's empty)
                    # Copy the arc's next state into the truth table
                    if not expression or logic_eval(self.input_names, input_combo, expression):
                        row["next_states"].append(arc["next_state"])
                
                # Process the current state to get the Moore output
                for output in self.output_names:
                    if state_datum["outputs"][output] == "1":
                        row[output] = "1"
                    else:
                        row[output] = "0"

                row["used"] = True
            
            # If the state combo is unused:
            else:
                # Don't care next state / output
                row["next_states"].append("x" * len(state_combo))
                for output in self.output_names:
                    row[output] = "x"
                row["used"] = False

            rows.append(row)
                
        return rows

                



            
                    
                