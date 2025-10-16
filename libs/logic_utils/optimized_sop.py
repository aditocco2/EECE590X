from logic_utils import qm2

def optimized_sop(inputs, output_column, treat_dc_like_0 = False):
    
    """
    Quine-McCluskey optimized sum of products finder
    This is basically a wrapper for the qm2 file that adds named inputs and outputs

    Arguments:
    inputs: list of ordered input names like ["a", "b", "c", "d"]
    output_column: output truth table column like "1010001110100011"

    Returns:
    optimized sum of products in Boolean form like "bc + b'd'"    
    """

    ones, zeros, dc = [], [], []

    for i in range(len(output_column)):
        if output_column[i] == "1":
            ones.append(i)
        elif output_column[i] == "0" or (output_column[i] == "x" and treat_dc_like_0):
            zeros.append(i)
        elif output_column[i].lower() == "x":
            dc.append(i)
    
    # Outputs a list like ['X0X0', 'X11X']
    qm2_output = qm2.qm(ones, zeros, dc)

    # Convert these to Boolean algebra form with the inputs
    terms = []
    for qm_term in qm2_output:

        term = ""

        for input, char in zip(inputs, qm_term):
            if char == "1":
                term += input
            elif char == "0":
                term += f"{input}'"
            # For don't care, just don't include the letter
    
        terms.append(term)
    
    sop = " + ".join(terms)

    return sop