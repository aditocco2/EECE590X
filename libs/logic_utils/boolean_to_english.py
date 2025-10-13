import re

def to_english(inputs, expression):
    
    """
    Turns a typical Boolean algebra expression (like (a + bc)') into its
    English form

    inputs: list of inputs like ["a", "b", "c"]
    expression: string for Boolean expression like "(a + bc)'"

    returns: English expression like "not (a or b and c)"
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
    expression = expression.replace("'", " not ")
    expression = expression.replace("+", " or ")
    expression = expression.replace("*", " and ")
    expression = expression.replace("^", " xor ")

    return expression