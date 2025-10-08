import re

def to_bitwise(inputs, expression):
    
    """
    Turns a typical Boolean algebra expression (like (a + bc)') into its
    bitwise operation form

    inputs: list of inputs like ["a", "b", "c"]
    expression: string for Boolean expression like "(a + bc)'"

    returns: "Bitwise Boolean" expression like "~(a+b&c)"
    """

    # Purge expression of spaces
    expression = expression.replace(" ", "")

    # Artificially put *s in places where the AND is implied
    for i in inputs:
        expression = re.sub(rf"\)('?){i}", rf")\1*{i}", expression)
        expression = re.sub(rf"{i}('?)\(", rf"{i}\1*(", expression)
        # Gotta account for combos of multiple inputs
        for j in inputs:
            expression = re.sub(rf"{i}('?){j}", rf"{i}\1*{j}", expression)

    # If ' appears after a term, move it before
    # ex: ab' -> a'b
    # LEAVE A SPACE SO BELOW ALGORITHM DOESN'T PICK UP THE )' PATTERN
    for i in inputs:
        expression = re.sub(f"{i}'", f" '{i}", expression)

    # If ' appears after (), move it before the appropriate group
    # ex: (a+(b)')' -> '(a+'(b))
    # expression = re.sub(r"(\(.*\))'", r"'\1", expression) # for outer 
    # expression = re.sub(r"(\([^(]*?\))'", r"'\1", expression) # for inner
    for i in range(1, len(expression)):
        if expression[i] == "'" and expression[i-1] == ")":
            j = i-1
            paren_depth = 1
            while paren_depth > 0:
                j -= 1
                if expression[j] == ")":
                    paren_depth += 1
                elif expression[j] == "(":
                    paren_depth -= 1
            expression = expression[:j] + "'" + expression [j:i] + expression[i+1:]

    # Purge expression of spaces AGAIN
    expression = expression.replace(" ", "")

    # Finally replace the operators with their bitwise equivalents
    expression = expression.replace("'", "~") # NOT
    expression = expression.replace("+", "|") # OR
    expression = expression.replace("*", "&") # AND
                                # ^ as XOR is fine

    return expression

# Sanity Check
# print(to_bitwise(["a", "b", "c", "d"], "(a(b^c)')'"))
# print(to_bitwise(["a", "b", "c", "d"], "(b'+c)d'"))
# print(to_bitwise(["a", "b", "c", "d"], "a'bc'd"))

def logic_eval(inputs, input_values, expression):
    """
    Evaluates a Boolean expression to return either 0 or 1.

    inputs: list of inputs like ["a", "b", "c"]
    input_combo: string or list w/  current combination of those inputs,
    like "101", meaning a=1, b=1, c=1
    expression: Boolean expression like like "(a + bc)'"
    """
    expression = to_bitwise(inputs, expression)

    # Convert from string to list if necessary
    if type(input_values) == str:
        input_values = [i for i in input_values]

    # Replace inputs with their current values of 0 or 1
    for i, iv in zip(inputs, input_values):
        expression = expression.replace(i, iv)
    
    output = eval(expression)

    # isolate LSB to avoid weird Python integer jank
    output &= 1

    return output

print(logic_eval(["a", "b", "c"], "101", "~a^c"))