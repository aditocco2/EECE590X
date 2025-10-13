from TruthTableHTML.html_tt import html_tt
from logic_utils import logic_eval, boolean_to_english
from logic_utils.optimized_sop import optimized_sop
from schemdraw.parsing import logicparse
import itertools
import json
import re

class FSM():

    """
    Class representing FSM data from FSM Explorer (https://ws.binghamton.edu/dsummer/fsmexplorer/)
    Used for converting data from FSM drawing to:
        - HTML truth table
        - Boolean expressions for the state/output logic
        - ...

    DISCLAIMERS:
        - Currently only works with Moore FSMs, which are used exclusively in EECE251.
            May add Mealy outputs for EECE351 compatibility later.
        - States in FSM must be named after their respective binary state encodings, like "00" or "1".
        - Outputs must be specified with their output names, i.e. "F=1". Implicit 0 is fine.
        - To make a truth table, the FSM must be properly specified, including arcs that go back to the same state.
    """

    """ 
    Members:
    input_names: inputs external to the FSM, like ["a", "b"]
    num_inputs: number of inputs
    input_combos: all possible combinations of input, like ["00", "01", "10"]
    state_bit_names: names of separated bits of the current state, 
        like ["Q1", "Q0"]
    next_state_bit_names: names of separated bits of the NEXT state, 
        like ["Q1+", "Q0+"]
    num_state_bits: number of state bits
    state_bit_combos: all possible combinations of the state bits, 
        even if they are not used, like ["00", "01", "10", "11]
    output_names: names of the FSM's external outputs, like ["F", "G"]
    output_columns: dictionary of columns of TT outputs as strings like "000011xx"
    output_expressions: dictionary of optimized sums of products

    fsm_json: JSON dictionary of FSM data straight from FSM Explorer
    arc_data: List of dictionaries showing each state and its associated arcs
    rows: List of dictionaries showing all possible input/state combos
        and their outputs
    """

    def __init__(self, filename, fsm_name = "FSM", state_notation = "Q"):
        self.fsm_name = fsm_name
        self.load_fsm_from_json(filename, state_notation)

    def load_fsm_from_json(self, filename, state_notation = "Q"):
        with open(filename, "r") as f:
            self.fsm_json = json.load(f)
        self.get_inputs_from_json()
        self.get_outputs_from_json()
        self.get_states_from_json(state_notation)
        self.get_arc_data_from_json()
        self.evaluate_all_combos()
    

    def get_arc_data_from_json(self):

        arc_data = []

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
                    
            arc_data.append(current_state_data)
        
        self.arc_data = arc_data
        return arc_data
    

    def get_states_from_json(self, notation = "Q"):
        self.state_names = []
        for node in self.fsm_json["fsmNodes"]:
            self.state_names.append(node["stateName"])
        self.state_names = sorted(self.state_names)

        self.num_state_bits = len(self.state_names[0])
        self.state_bit_combos = [f"{i:0{self.num_state_bits}b}" for i in range(2 ** self.num_state_bits)]

        # Make state bit names like Q1, Q0, Q1+, Q0+
        self.state_bit_names = [notation + str(i) for i in range(self.num_state_bits)]
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
            
        self.num_inputs = len(self.input_names)
        self.input_combos = [f"{i:0{self.num_inputs}b}" for i in range(2 ** self.num_inputs)] \
                            if self.num_inputs > 0 else [""]


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


    def evaluate_all_combos(self):

        """
        Evaluates all combinations of state and input to find out what the
        next state and output should be.
        """

        rows = []

        # make all possible combinations of state with input
        all_combos = itertools.product(self.state_bit_combos, self.input_combos)

        # Then drill the logic
        for combo in all_combos:

            state_combo = combo[0]
            input_combo = combo[1]
            
            row = {}
            row["state"] = state_combo
            for i in range(len(input_combo)):
                row[self.input_names[i]] = input_combo[i]
            # A list, so we can check for improperly specified FSMs
            row["next_states"] = []

            # Get the dictionary with the appropriate state
            state_datum = [d for d in self.arc_data if d["state"] == state_combo]

            # If the state combo is used, figure out the appropriate next state
            if state_datum:
                state_datum = state_datum[0]

                # Process the arc to get the next state
                arcs = state_datum["arcs"]
                for arc in arcs:
                    expression = arc["expression"]
                    # If the expression on the arc evaluates to true (or it's empty)
                    # Copy the arc's next state into the truth table
                    if not expression or logic_eval.logic_eval(
                                        self.input_names, input_combo, expression):
                        # 6 levels of indentation let's go
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
        
        self.rows = rows
        return rows
    

    def make_output_columns(self):
    
        # Initialize dictionary of empty output columns
        output_columns = {}
        for name in self.next_state_bit_names + self.output_names:
            output_columns[name] = ""

        # Start with next_state
        for row in self.rows:
            # Check for improperly specified states
            if len(row["next_states"]) == 0:
                raise Exception(f"No state specified for the following row: {row}")
            elif len(row["next_states"]) > 1:
                raise Exception(f"Multiple states specified for the following row: {row}")
            else:
                next_state = row["next_states"][0]
                for i, next_state_bit in zip(range(self.num_state_bits), self.next_state_bit_names):
                    output_columns[self.next_state_bit_names[i]] += next_state[i]

        # Then do Moore outputs
        for row in self.rows:
            for output in self.output_names:
                output_columns[output] += row[output]
    
        self.output_columns = output_columns
        return output_columns


    def make_html_truth_table(self):

        """Returns HTML truth table of FSM next state and outputs."""

        if not hasattr(self, "output_columns"):
            self.make_output_columns()
        
        all_out_names = self.next_state_bit_names + self.output_names
        cols = [self.output_columns[key] for key in all_out_names]

        headers = self.state_bit_names + self.input_names \
                  + self.next_state_bit_names + self.output_names
        
        html_output = html_tt(cols, headers)

        return html_output
    
    def find_output_expressions(self):
        
        """
        Returns a dictionary of each output (including next state) and its 
        optimized sum of products.
        """

        if not hasattr(self, "output_columns"):
            self.make_output_columns()

        inputs = self.state_bit_names + self.input_names
        outputs = self.next_state_bit_names + self.output_names
        output_expressions = {}

        for output in outputs:
            col = self.output_columns[output]
            output_expressions[output] = optimized_sop(inputs, col)

        self.output_expressions = output_expressions
        return output_expressions
    
    def write_output_expressions_to_file(self, filename = "outputs.txt", clear=False):

        """
        Writes the logic for the FSM's output expressions to a file,
        so that circuit diagrams can be made for it if need be.

        filename: text file to write to
        clear: whether or not to empty the file before writing to it
        """
        
        # Clear the file
        if clear:
            with open(filename, "w") as f:
                pass

        f = open(filename, "a") # Append mode to not overwrite previous stuff
        f.write(f"{self.fsm_name} outputs:\n")

        if not hasattr(self, "output_expressions"):
            self.find_output_expressions()
        
        for output_name in self.output_expressions:
            output_expression = self.output_expressions[output_name]
            f.write(f"{output_name} = {output_expression}\n")
        
        f.write("\n")

        f.close()


    def follow(self, sequence, starting_state):
        
        """
        Simulates the FSM, following the sequence of inputs from the starting state.
        Returns the ending state.

        sequence: can be multiple types:
            - list of strings for more than one input
            - string for one input
            - number of iterations for no inputs
        starting_state: string for starting state of the FSM
        """

        # Process sequence argument into a list
        if type(sequence) is int and self.num_inputs == 0:
            sequence_length = sequence
            sequence = ["" for _ in range(sequence)]
        elif type(sequence) is str and self.num_inputs == 1:
            sequence_length = len(sequence)
            sequence = [i for i in sequence]
        elif type(sequence) is list and self.num_inputs >= 1:
            sequence_length = len(sequence)
        else:
            raise Exception("sequence argument type doesn't match number of inputs")

        state = starting_state

        # Move through the sequence
        for step in range(sequence_length):
            # If there are inputs, check the state and its inputs
            # if self.num_inputs >= 1:

            # Find the row containing the state and its inputs
            inputs = sequence[step]
            row = self.find_row(state, inputs)

            # Check to make sure it's properly specified
            if len(row["next_states"]) != 1:
                raise Exception(f"state {state} is improperly specified")
            else:
                next_state = row["next_states"][0]
                state = next_state
        
        return state


    def find_row(self, state, input_combo=""):

        """
        Process the dictionaries to find a row with a specific state and input combo
        """

        for row in self.rows:

            # Go through all inputs and make sure they are correct
            correct_input = True
            for input, input_value in zip(self.input_names, input_combo):
                if row[input] != input_value:
                    correct_input = False
            
            # Ensure state is correct
            correct_state = (row["state"] == state)

            if correct_input and correct_state:
                return row
    
        # Error if nothing found
        raise Exception("No state found")
            
    def find_outputs(self, state):

        """
        Returns the outputs for a given state
        """

        state_datum = [d for d in self.arc_data if d["state"] == state][0]
        return state_datum["outputs"]

